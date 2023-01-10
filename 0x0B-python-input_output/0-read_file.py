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
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
