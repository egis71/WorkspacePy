# -*- coding: utf-8 -*-
import sys


def main(file_name):
    file = open(file_name)
    # print(file.__doc__)
    # print(file.name)
    # print(file)
    for l in file:
        print(l, end='')
    file.close()


if __name__ == "__main__":
    # execute only if run as a script
    # print(sys.argv)

    # file_name = None
    # if len(sys.argv) == 2:
    #     file_name = sys.argv[1]
    file_name = len(sys.argv) == 2 and sys.argv[1]

    if file_name:
        main(file_name)
