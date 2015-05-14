import sys


def main():
    file_name = sys.argv[-1]
    file_two = sys.argv[-2]
    file_o = open(file_name, "r")
    file_o2 = open(file_two, "r")
    content = file_o.read()
    content_2 = file_o2.read()
    print(content + "\n\n")
    print(content_2)
    file_o.close()

if __name__ == '__main__':
    main()
