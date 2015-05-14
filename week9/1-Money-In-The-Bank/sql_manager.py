import sqlite3
from Client import Client

class Manager:

    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def change_message(self, new_message, logged_user):
        logged_user_id = logged_user.get_id()
        update_sql = "UPDATE clients SET message = ? WHERE id = ?"
        self.cursor.execute(update_sql, (new_message, logged_user_id))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        logged_user_id = logged_user.get_id()
        update_sql = "UPDATE clients SET password = ? WHERE id = ? "
        self.cursor.execute(update_sql, (new_pass, logged_user_id))
        self.conn.commit()

    def register(self, username, password):
        insert_sql = "insert into clients (username, password) values (?, ?)"
        self.cursor.execute(insert_sql, (username, password))
        self.conn.commit()

    def login(self, username, password):
        select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
        self.cursor.execute(select_query, (username, password))
        user = self.cursor.fetchone()
        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
