#!/usr/bin/python3

def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    """
    with open(filename, 'a', encoding="utf-8") as newFile:
        return (newFile.write(text))
