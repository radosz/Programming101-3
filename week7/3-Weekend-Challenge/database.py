import sqlite3

create_table_servers = """
CREATE TABLE IF NOT EXISTS ServerInfo(id INTEGER PRIMARY KEY, url TEXT unique,server TEXT)
"""
insert_into_query = """
INSERT INTO ServerInfo ({})
VALUES ("{}","{}")
"""

create_table_soup = """
CREATE TABLE IF NOT EXISTS soup(id INTEGER PRIMARY KEY, url TEXT unique)
"""
insert_into_soup = """
INSERT INTO soup ({})
VALUES ("{}")
"""

select_query = """
SELECT * FROM ServerInfo
"""

search_query = """
SELECT * FROM ServerInfo WHERE server like "%{}%";
"""
soup_url_query = """SELECT url
FROM soup"""


class Database():

    def __init__(self, db_name="bg_servers.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute(create_table_servers)
        self.all_s = self.cursor.execute(select_query)

    def soup_url(self):
        urls = []
        q = self.cursor.execute(soup_url_query)
        for row in q:
            urls.append(row["url"])
        return urls

    def create_table_soup(self):
        self.cursor.execute(create_table_soup)

    def insert_into_soup(self, links):
        try:
            for link in links:
                print("Save in Database", link)
                self.cursor.execute(insert_into_soup.format("url", link))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def insert(self, values):
        try:
            a, b = values
            self.cursor.execute(insert_into_query.format("url,server", a, b))
        except Exception:
            pass

    def commit(self):
        self.conn.commit()

    def view_all(self):
        r = self.cursor.execute(select_query)
        for row in r:
            print("{}||{}||{}".format(row["id"], row["url"], row["server"]))

    def search(self, item):
        r = self.cursor.execute(search_query.format(item))
        return r

    def create_server_list(self, cursor):
        return [item["server"] for item in cursor]

    def create_url_list(self, cursor):
        return [item["url"] for item in cursor]

    def create_server_list_all(self):
        return [item["server"] for item in self.all_s]

    def create_url_list_all(self):
        return [item["url"] for item in self.all_s]

    def close_db(self):
        self.conn.close()


def main():
    db = Database("proben.db")
    db.create_table_soup()
    db.insert_into_soup("abv.bg")
    db.insert(("abv1.bg", "Apache"))
    db.insert(("gbg2.bg", "Apache"))
    db.insert(("hit3.bg", "Apache"))
    r = db.search("Apache")
    print(db.create_server_list(r))
    db.view_all()
    db.close_db()

if __name__ == '__main__':
    main()
