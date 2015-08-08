import datetime
import time


def accepts(*types):
    def accepter(f):
        def decorated(*args):
            for index, (a, t) in enumerate(zip(args, types)):
                if type(a) != t:
                    raise TypeError(
                        "Argument {} of {} is not {}!".format(index, f.__name__, t.__name__))
            return f(*args)
        return decorated
    return accepter


@accepts(str, int)
def say_hello(name, age):
    return "Hello, I am {} {}".format(name, age)


def caesar(text, n):
    alphabet_l = "abcdefghijklmnopqrstuvwxyz"
    alphabet_c = alphabet_l.upper()
    answ = ""
    for i in text:
        if alphabet_l.find(i) != -1 and alphabet_l.find(i) != len(alphabet_l) - 1:
            answ += alphabet_l[alphabet_l.find(i) + n]
        elif alphabet_c.find(i) != -1 and alphabet_c.find(i) != len(alphabet_c) - 1:
            answ += alphabet_c[alphabet_c.find(i) + n]
        elif alphabet_l.find(i) == len(alphabet_l) - 1:
            answ += alphabet_l[0]
        elif alphabet_c.find(i) == len(alphabet_c) - 1:
            answ += alphabet_c[0]
        else:
            answ += i
    return answ


def encrypt(n):
    def decorated(func):
        def dec():
            return caesar(func(), n)
        return dec
    return decorated


def log(path):
    def decorated(func):
        def dec():
            input_str = "{} was called at {}".format(
                func.__name__, str(datetime.datetime.now()))
            with open(path, "a")as myfile:
                myfile.write(input_str + "\n")
                myfile.close()
            return func()
        return dec
    return decorated


def performance(path):
    def decorated(func):
        def dec():
            start = time.time()
            func()
            end = time.time()
            input_str = "{} was called and took {} seconds to complete".format(
                func.__name__, str(end - start))
            with open(path, "a")as myfile:
                myfile.write(input_str + "\n")
                myfile.close()
            return func()
        return dec
    return decorated


@performance('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

# Implement memorize


def fib(n):
    if n == 0:
        raise Exception
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
