import sys


def main():
    file_name = sys.argv[-1]
    file_o = open(file_name, "r")
    content = file_o.read()
    print(content)
    file_o.close()

if __name__ == '__main__':
    main()
