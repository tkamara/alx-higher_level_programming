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
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(f.read(), end='')
