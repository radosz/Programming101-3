import requests
from soupproducts import SoupProducts

TIMEOUT = 10
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

to_his = set()


class WebCrawling:

    stop_crawl = -1

    def __init__(self, url, dot=".bg"):
        self.dot = dot
        self.url = self.__filter_url(url)
        self.all_urls = []

    def __get_url(self, link):
        link_url = requests.head(
            link, timeout=TIMEOUT,
            headers=USER_AGENT)
        if str(link_url.status_code).startswith("3"):
            link = link_url.headers['Location']
        return link

    def __filter_url(self, link):
        link = self.__get_url(link)
        web = link.split("/")
        if len(web) > 2:
            if web[2].find(self.dot):
                domain = web[2].split(".")[-2]
                web = web[0] + "//" + "www." + domain + self.dot + "/"
            return web

    def __add__to_his(self, link, limit):
        url = self.__get_url(link)
        web = self.__filter_url(url)
        to_his.add(web)
        WebCrawling.stop_crawl = len(to_his)

    def crawling(self, limit=9999):
        # print(WebCrawling.stop_crawl)

        if WebCrawling.stop_crawl == -1:
            sp = SoupProducts(self.url, 10000)
            sp.generate_all_urls()
            self.to_crawl = sp.get_all_unique()
            WebCrawling.stop_crawl += 1

        if WebCrawling.stop_crawl == limit:
            return

        try:
            link = self.to_crawl.pop()
            self.__add__to_his(link, limit)
            self.crawling(limit)
        except IndexError:
            return
        except Exception:
            link = self.to_crawl.pop()
            self.__add__to_his(link, limit)
            self.crawling(limit)


def main():

    craw = WebCrawling("http://start.bg")
    craw.crawling(10)

    print(len(to_his))
    print("to_his", to_his)

if __name__ == '__main__':
    main()
