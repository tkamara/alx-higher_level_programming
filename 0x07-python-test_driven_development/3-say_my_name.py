#!/usr/bin/python3
"""
Function that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints name

    Parameters:
        first_name(str): the first name
        last_name(str): the surname

    Return:
        My name is ...
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
