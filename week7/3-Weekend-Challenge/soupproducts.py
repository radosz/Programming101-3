import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from database import Database

TIMEOUT = 5
LIMIT = 60000
USER_AGENT = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}

visited = []
all_urls = []


class SoupProducts:

    def __init__(self, url, limit=LIMIT):
        self.products = []
        self.limit = limit
        self.url = url
        self.products += self.__prepare_soup(url, limit)
        self.soup = []
        self.domain = self.__get_domain()

    def __get_domain(self):
        return urlparse(self.url).netloc

    def __head(self, url):
        head = requests.get(
            url, timeout=TIMEOUT, headers=USER_AGENT)
        if head.url.find("start.bg") == -1:
            raise Exception
        if head.url not in visited:
            visited.append(head.url)
            all_urls.append(head.url)
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
                if link.get('href').find("javascript:") == -1:
                    products.append(link.get('href'))
                    limit -= 1
                else:
                    continue
        return self.__fix_products(products)

    def __to_find(self):
        url = urlparse(self.url)
        return url.scheme + "://" + url.netloc + url.path

    def __fix_products(self, products):
        url = self.__to_find()
        fixed = []
        for product in set(products):
            if product.find("http") == -1:
                fixed.append(url + product)
            elif product.find("http") > -1:
                if self.__get_domain() in urlparse(product).netloc:
                    fixed.append(product)
#        products = [
#            url + x for x in products if x.find("http") == -1]
        print(fixed[-1])
        return fixed

    def get_products(self):
        return self.products

    def next_soup(self):
        nexturl = self.products.pop()
        return SoupProducts(nexturl).get_products()

    def generate_all_urls(self):
        while len(all_urls) <= self.limit:
            try:
                for link in self.next_soup():
                    all_urls.append(link)
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
        return all_urls

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
        return set(all_urls)

    def save_uniqe_in_db(self, db_name):
        db = Database(db_name)
        db.create_table_soup()
        links = self.get_all_unique()
        db.insert_into_soup(links)


def main():
    sp = SoupProducts("http://start.bg")
    sp.generate_unique_urls()
    sp.save_uniqe_in_db("bg_servers.db")
    print("all", len(all_urls))
    print("unique", len(sp.get_all_unique()))
    print("list", sp.get_all_unique())

if __name__ == '__main__':
    main()
