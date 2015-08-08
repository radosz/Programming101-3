import os
import sys
import unittest

sys.path.append("..")
from sql_manager import Manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        os.system("cat bank.sql|sqlite3 bank_test.db")
        self.sm = Manager("bank_test.db")
        self.sm.register('Tester', '123')

    def tearDown(self):
        os.system("rm bank_test.db")

    def test_sql_injection(self):
        self.assertEqual(self.sm.login("Tester", "' OR 1 = 1 --"), False)

    def test_register(self):
        self.sm.register('Dinko', '123123')

        self.sm.cursor.execute(
            'SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123123'))
        users_count = self.sm.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.sm.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.sm.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.sm.login('Tester', '123')
        new_message = "podaivinototam"
        self.sm.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.sm.login('Tester', '123')
        new_password = "12345"
        self.sm.change_pass(new_password, logged_user)

        logged_user_new_password = self.sm.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
