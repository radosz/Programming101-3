import os
from Xlib import display


def chain(iterable_one, iterable_two):
    for element in iterable_one:
        yield element
    for element_two in iterable_two:
        yield element_two


def compress(itterable, mask):
    for element, m in zip(itterable, mask):
        if m == True:
            yield element


def cycle(iterable):
    itr = iter(iterable)
    while True:
        try:
            element = next(itr)
            yield element
        except StopIteration:
            itr = iter(iterable)

# Book generator


def read_book(book):
    book_file = open(book, "r")
    str_b = ""
    for character in book_file:
        if not character.startswith("#"):
            str_b += character
        elif character.startswith("#"):
            str_b += character
            input()
            yield str_b
    yield str_b
    str_b = ""

    book_file.close()


def books(path):
    files_in_dir = os.listdir(path)
    for myfile in files_in_dir:
        part = myfile.split(".")
        if part[1] == "txt":
            yield read_book(path + myfile)


def book(path):
    for txt in books(path):
        for line in txt:
            yield line
