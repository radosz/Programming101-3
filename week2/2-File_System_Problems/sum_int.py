import sys


def main():
    split = " "
    filename = sys.argv[-1]
    int_list = open(filename, "r")
    all_char = int_list.read()
    spl_all = all_char.split(split)
    all_int = [int(x) for x in spl_all]
    int_list.close()
    print(sum(all_int))

if __name__ == '__main__':
    main()
