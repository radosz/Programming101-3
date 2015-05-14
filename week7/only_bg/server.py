import requests
import traceback
import crawl
import plot_info as plt
from database import Database
import os

TIMEOUT = 10
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

servers_types = ["nginx", "IIS", "Apache", "lighttpd"]


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
        self.servers = []
        self.__his = self.__scan_web_servers(limit)

    def get_histogram(self):
        return self.__his

    def __scan_web_servers(self, limit):
        scan_sites = 0
        for link in crawl.to_his:
            try:
                if link not in self.visited:
                    link_url = requests.head(
                        link, timeout=TIMEOUT,
                        headers=USER_AGENT, allow_redirects=True)
                    self.servers.append(link_url.headers['Server'])
                    self.visited.add(link)
                    scan_sites += 1
                self.save_in_db()
            except Exception:
                self.exc.append(
                    "URL: " + link + "\n" + traceback.format_exc())
            if len(self.servers) == limit:
                self.servers.append(str(scan_sites))
                break
        return self.histogram()

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
        db = Database()
        for v, s in zip(self.visited, self.servers):
            db.insert((v, s))
        db.close_db()

    @staticmethod
    def load_db():
        db = Database()
        servers = db.create_server_list_all()
        crawl.urls = db.create_url_list_all()
        servers = ServersHistogram.prepare_server_lst(servers)
        return create_histogram(servers)


def main():

    load_his = ServersHistogram.load_db()
    ServersHistogram.print_stats(load_his)

    try:
        craw = crawl.WebCrawling("http://start.bg")
        craw.crawling(2000)
    except Exception:
        print(crawl.to_his)
        pass

    sh = ServersHistogram(crawl.to_his)
    his = sh.get_histogram()
    ServersHistogram.save_fig(his)
    sh.save_to_file()


if __name__ == '__main__':
    main()
