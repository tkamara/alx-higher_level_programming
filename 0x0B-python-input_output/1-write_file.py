#!/usr/bin/python3
"""
writing a string to a text file
"""


def write_file(filename="", text=""):
    with open('my_first_file.txt', 'w') as f:
        data = f.write(text)
        return (data)
