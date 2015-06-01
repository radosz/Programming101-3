import sys
import os
import math


def convert_size(size,work_dir):
    size_name = ("KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    if (s > 0):
        return "{} size is: {} {}".format(work_dir,s,size_name[i])
    else:
        return '0B'


def main():
    path = sys.argv[-1]
    try:
        work_dir = os.getcwd()
        os.chdir(path)
        files_in_dir = os.listdir(os.getcwd())
        size_list = [os.path.getsize(path + "/" + x) for x in files_in_dir]
        size_hs = convert_size(sum(size_list),os.getcwd())
        os.chdir(work_dir)
        print(size_hs)
    except FileNotFoundError:
        print("File or dir not found !")


if __name__ == '__main__':
    main()
