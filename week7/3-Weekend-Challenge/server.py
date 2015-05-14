import requests
import traceback
from bs4 import BeautifulSoup
import plot_info as plt
from database import DataBase
import os

TIMEOUT = 3
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

servers_types = ["nginx", "IIS", "Apache", "lighttpd"]
scan_sites = 0
urls = set()
v_url = []
all_links = []


def create_histogram(servers):
    all_count = 0
    count = 0
    his = {}
    for type_s in servers_types:
        for s in servers[:-1]:
            if s.find(type_s) > -1:
                count += 1
        his[type_s] = count
        all_count += his[type_s]
        count = 0
    his['Others'] = int(servers[-1]) - all_count
    return his


class ServersHistogram:

    def __init__(self, urls, limit=9999):
        self.exc = []
        self.visited = set()
        web = ""

        if not limit:
            limit = len(urls)

        scan_sites = 0
        self.servers = []

        for link in urls:
            try:
                link_url = requests.head(
                    link, timeout=TIMEOUT,
                    headers=USER_AGENT)

                if str(link_url.status_code).startswith("3"):
                    web = link_url.headers['Location']
                else:
                    web = link.split("/")
                    web = web[0] + "//" + web[1] + web[2] + "/"

                if web not in self.visited:
                    link_url = requests.head(
                        web, timeout=TIMEOUT,
                        headers=USER_AGENT)
                    self.servers.append(link_url.headers['Server'])
                    self.visited.add(web)
                    scan_sites += 1
                self.save_in_db()
            except Exception:
                self.exc.append(
                    "URL: " + web + "\n" + traceback.format_exc())

            if len(self.servers) == limit:
                self.servers.append(str(scan_sites))
                break

    @staticmethod
    def load(full_path):
        servers = []
        with open(full_path, "r") as server_file:
            str_s = server_file.read()
            servers = str_s.split("\n")
            digit = servers[-1]
            servers = [s[:s.find("http://")] for s in servers]
            servers.append(digit)
            servers = ServersHistogram.prepare_server_lst(servers)
            server_file.close()
        return servers

    @staticmethod
    def file_to_histogram(full_path):
        servers = ServersHistogram.load(full_path)
        his = create_histogram(servers)
        return his

    @staticmethod
    def prepare_server_lst(servers):
        result = []
        for type_s in servers_types:
            result += [s.strip() for s in servers if s.find(type_s) > -1]
        n = str(len(servers))
        result.append(n)
        return result

    def save_to_file(self):
        spaces = max([len(str(x)) for x in self.servers]) + 5
        to_str = "\n".join([str(s + " " * (spaces - len(s)) + v)
                            for v, s in zip(self.visited, self.servers)])
        with open("stats.txt", "w") as s_file:
            s_file.write(to_str)
            s_file.write("\n" + self.servers[-1])
            s_file.close()
        with open("errors.txt", "w") as err:
            err.write("\n".join(self.exc))
            err.close()

    def histogram(self):
        servers = ServersHistogram.prepare_server_lst(self.servers)
        return create_histogram(servers)

    @staticmethod
    def print_stats(hist, bar_color=plt.color_bar, text_color=plt.color_text, width=plt.width):
        plt.width = width
        plt.color_bar = bar_color
        plt.color_text = text_color
        plt.print_plot(hist)

    @staticmethod
    def save_fig(hist, bar_color=plt.color_bar, text_color=plt.color_text, width=plt.width):
        plt.save_histogram(hist, os.getcwd())

    def save_in_db(self):
        db = DataBase()
        for v, s in zip(self.visited, self.servers):
            db.insert((v, s))
        db.close_db()

    @staticmethod
    def load_db():
        db = DataBase()
        result = db.search("")
        servers = db.create_server_list(result)
        r = db.search("")
        v_url = db.create_url_list(r)
        servers = ServersHistogram.prepare_server_lst(servers)
        return create_histogram(servers)


class WebCrawling:

    def __init__(self, url):

        if url[-1] != "/":
            url = url + "/"
        self.url = url

        self.get_url = requests.get(url, timeout=TIMEOUT, headers=USER_AGENT)
        self.html = self.get_url.text
        self.all_urls = []

    def crawling(self):
        soup = BeautifulSoup(self.html)
        for link in soup.find_all('a'):
            self.all_urls.append(link.get('href'))

        for link in self.all_urls:
            try:
                domain = self.url[self.url.find("://") + 3: -1]
                if link.find(domain) > -1 and link not in v_url:
                    v_url.append(link)
                    urls.add(link)
                if isinstance(link, str) and link not in v_url:
                    if link.find("http") == -1:
                        all_links.append(self.url + link)
            except AttributeError:
                pass

        if urls:
            http = urls.pop()
            try:
                return WebCrawling(http).crawling()
            except Exception:
                http = urls.pop()
                return WebCrawling(http).crawling()


class Cron:

    @staticmethod
    def start_every_day_at(hour, minute, file_name):
        Cron.__create_task_file(file_name)
        cmd_start = "./start_at"
        cmd_remove = "./start_at --remove"
        if minute <= 9:
            minute = "0" + str(minute)

        if hour <= 9:
            hour = "0" + str(hour)

        w_dir = os.getcwd()

        task = "{} {} * * * env DISPLAY=:0 {}/task.sh".format(
            minute, hour, w_dir, os.getcwd())
        with open("start_at.crontab", "w") as start:
            start.write(task)
            start.close()
        # os.system(cmd_remove)
        os.system(cmd_start)

    @staticmethod
    def __create_task_file(command):
        file_str = """
#!/bin/sh
#!/bin/python3.4
cd "{}"
python3 "{}"
""".format(os.getcwd(), command)
        command = "chmod +x task.sh"
        with open("task.sh", "w") as start:
            start.write(file_str)
            start.close()
        os.system(command)


def main():
    his = ServersHistogram.load_db()
    ServersHistogram.save_fig(his)
    Cron.start_every_day_at(12, 30, "server.py")
    craw = WebCrawling("http://start.bg")
    craw.crawling()
    sh = ServersHistogram(all_links)
    ServersHistogram.save_fig(his)
    sh.save_to_file()


if __name__ == '__main__':
    main()
