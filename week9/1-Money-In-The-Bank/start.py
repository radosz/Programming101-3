import hashlib
import getpass
from sql_manager import Manager
sm = Manager("bank.db")

WrongPassLimit = 5


class Pass:

    @classmethod
    def validate(cls, password):
        cls.is_number(password)
        cls.isCaptital(password)
        if len(password) < 8:
            raise PasswordLenException

    @classmethod
    def is_number(cls, password):
        for c in password:
            if c.isnumeric():
                return True
        raise NotDigitInPasswordException

    @classmethod
    def isCaptital(cls, password):
        for c in password:
            if c.isupper():
                return True
        raise NotUpperCharException


def main_menu():
    print(
        "Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass(
                prompt='Enter you password: ', stream=None)

            Pass.validate(password)
            password = hashlib.md5(password.encode()).hexdigest()
            sm.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            login_count = 0
            username = input("Enter your username: ")
            password = getpass.getpass(
                prompt='Enter you password: ', stream=None)

            logged_user = sm.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                login_count += 1
                print("Login failed")

            if login_count == WrongPassLimit:
                raise BruteForceException

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sm.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sm.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    main_menu()

if __name__ == '__main__':
    main()


class PasswordLenException(Exception):
    pass


class NotDigitInPasswordException(Exception):
    pass


class NotUpperCharException(Exception):
    pass


class BruteForceException(Exception):
    pass
