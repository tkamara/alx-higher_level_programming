#!/usr/bin/python3
"""
Reading text file
"""


def read_file(filename=""):
    """
    reads text file and prints to stdout

    Argument:
        filename(str): the file name
    """
    with open('my_file_0.txt') as f:
        for line in f:
            print(f.read(), end='')
