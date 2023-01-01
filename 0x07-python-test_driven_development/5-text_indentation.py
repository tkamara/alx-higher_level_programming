#!/usr/bin/python3
"""
Printing text with 2 new lines after certain characters
"""


def text_indentation(text):
    """
    Printing text with 2 new lines after characters

    Parameters:
    text(str): the text

    Return:
    text with the new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    line = text.replace(".", ".\n\n")
    line = line.replace("?", "?\n\n")
    line = line.replace(":", ":\n\n")

    test = line.splitlines(True)

    new_list = []

    for s in test:
        if s == "\n":
            new_list.append("\n")
        else:
            new_list.append(s.lstrip())
    print("".join(new_list), end="")
