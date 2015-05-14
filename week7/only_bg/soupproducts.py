import requests
from bs4 import BeautifulSoup
from copy import deepcopy
from database import Database

TIMEOUT = 1
LIMIT = 60000
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}


class SoupProducts:

    def __init__(self, url, limit=LIMIT):
        self.limit = limit
        self.url = url
        self.products = self.__prepare_soup(url, limit)
        self.soup = []
        self.domain = self.__get_domain()
        self.all_urls = []

    def __get_domain(self):
        web = self.url.split("/")
        if len(web) > 2:
            url = web[2].split(".")
            domain = url[-2]
            return domain + "." + url[-1]

    def __head(self, url):
        head = requests.get(
            url, timeout=TIMEOUT, headers=USER_AGENT)
        return head

    def get_html_doc(self, url):
        head = self.__head(url)
        return head.text

    def __prepare_soup(self, url, limit):
        products = []
        html = self.get_html_doc(url)
        soup = BeautifulSoup(html)
        for link in soup.find_all('a'):
            if link.get('href') and limit:
                products.append(link.get('href'))
                limit -= 1
        return self.__fix_products(products)

    def __to_find(self):
        web = self.url.split("/")
        http = web[0] + "//"
        if len(web) > 2 and self.url.find("http") == 0:
            url = web[2].split(".")
            domain = url[-2] + "." + url[-1]
            r_url = http + domain
            return r_url
        return self.url

    def __fix_products(self, products):
        url = self.__to_find()
        products = [
            url + "/" + x for x in products if x.find("http") == -1]
        return products

    def get_products(self):
        return self.products

    def next_soup(self):
        next = self.products.pop()
        if next.find(self.domain) > -1:
            return SoupProducts(next).get_products()

    def generate_all_urls(self):
        while len(self.all_urls) <= self.limit:
            try:
                self.all_urls += self.next_soup()
            except IndexError:
                break
            except TypeError:
                pass
            except requests.exceptions.ReadTimeout:
                pass
            except requests.exceptions.MissingSchema:
                pass
            except requests.exceptions.InvalidSchema:
                pass
            except requests.exceptions.ConnectionError:
                pass
        return self.all_urls

    def generate_unique_urls(self):
        while(len(self.get_all_unique())) <= self.limit:
            try:
                self.next_soup()
                self.generate_all_urls()
            except IndexError:
                break
            except Exception:
                pass
        return self.get_all_unique()

    def get_all_unique(self):
        return set(self.all_urls)

    def save_uniqe_in_db(self, db_name):
        db = Database(db_name)
        db.create_table_soup()
        print(len(self.get_all_unique()))
        for link in self.get_all_unique():
            db.insert_into_soup(link)


def main():
    sp = SoupProducts("http://start.bg", 200)
    sp.generate_unique_urls()
    sp.save_uniqe_in_db("bg_servers.db")
    print("all", len(sp.all_urls))
    print("unique", len(sp.get_all_unique()))
    print("list", sp.get_all_unique())
    '''
    all 60083
    unique 17918
    '''

if __name__ == '__main__':
    main()
