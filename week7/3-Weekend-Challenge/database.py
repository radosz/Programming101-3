import sqlite3
import json
create_table_servers = """
CREATE TABLE IF NOT EXISTS ServerInfo(id INTEGER PRIMARY KEY, url TEXT unique,server TEXT)
"""
insert_into_query = """
INSERT INTO ServerInfo ({})
VALUES ("{}","{}")
"""
select_query = """
SELECT * FROM ServerInfo
"""

search_query = """
SELECT * FROM ServerInfo WHERE server like "%{}%";
"""


class DataBase():

    def __init__(self):
        self.conn = sqlite3.connect("bg_servers.db")
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute(create_table_servers)

    def insert(self, values):
        try:
            a, b = values
            self.cursor.execute(insert_into_query.format("url,server", a, b))
            self.conn.commit()
        except Exception:
            pass

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

    def close_db(self):
        self.conn.close()


def main():
    db = DataBase()
    db.insert(("abv1.bg", "Apache"))
    db.insert(("gbg2.bg", "Apache"))
    db.insert(("hit3.bg", "Apache"))
    r = db.search("Apache")
    print(db.create_server_list(r))
    db.view_all()
    db.close_db()

if __name__ == '__main__':
    main()
