# generate_numbers.py
import sys
from random import randint


def main():
    numb = int(sys.argv[-1])
    numbers = [str(randint(1, 1000)) for x in range(numb)]
    filename = "numbers.txt"
    file = open(filename, "a")
    file.write(" ".join(numbers))
    file.close

if __name__ == '__main__':
    main()
