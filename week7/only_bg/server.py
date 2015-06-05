import requests
import crawl
import plot_info as plt
from urllib.parse import urlparse
from database import Database
import os

TIMEOUT = 10
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

servers_types = ["nginx", "IIS", "Apache", "lighttpd"]


def create_histogram(servers):
    print("his", servers)
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
    his['Others'] = len(servers) - all_count
    return his


class ServersHistogram:

    def __init__(self, urls, dot=".bg", limit=9999):
        self.dot = dot
        self.visited = set()
        self.v_links = set()
        self.to_db = set()
        self.servers = []
        crawl.to_his = urls
        self.__his = self.__scan_web_servers(limit)

    def get_histogram(self):
        return self.__his

    def __scan_web_servers(self, limit):
        print("Start scan")
        scan_sites = 0
        for link in crawl.to_his:
            try:
                if link not in self.visited:
                    link_url = requests.head(
                        link, timeout=TIMEOUT,
                        headers=USER_AGENT, allow_redirects=True)
                    self.visited.add(link)
                    url = urlparse(link_url.url)
                    u_link = self.get_domain(url)
                    if self.dot in link_url.url and u_link not in self.v_links:
                        self.v_links.add(u_link)
                        self.to_db.add(u_link)
                        self.servers.append(link_url.headers['Server'])
                        print(u_link, self.servers[-1])
                    else:
                        raise Exception
                    scan_sites += 1
            except Exception:
                pass
            if len(self.servers) == limit:
                break
        self.save_in_db()
        return self.histogram()

    # input from urlparse()
    def get_domain(self, url_p):
        s_netloc = url_p.netloc.split(".")
        u_link = url_p.scheme + "://" + s_netloc[-2] + "." + s_netloc[-1]
        return u_link

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

    def histogram(self):
        return create_histogram(self.servers)

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
        for v, s in zip(self.to_db, self.servers):
            db.insert((v, s))
        db.commit()
        db.close_db()

    @staticmethod
    def load_db():
        db = Database()
        servers = db.create_server_list_all()
        crawl.urls = db.create_url_list_all()
        return create_histogram(servers)


def main():

#    load_his = ServersHistogram.load_db()
#    ServersHistogram.print_stats(load_his)

    db = Database()
    db.create_table_soup()
    urls = db.soup_url()

    if len(urls) < 1:
        craw = crawl.WebCrawling("http://start.bg")
        craw.crawling()
        sh = ServersHistogram(crawl.to_his)
    else:
        sh = ServersHistogram(urls)

    his = sh.get_histogram()
    ServersHistogram.save_fig(his)


if __name__ == '__main__':
    main()
