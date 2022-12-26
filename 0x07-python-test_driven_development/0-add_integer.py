#!/usr/bin/python3
"""
A function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers

    Parameters:
        a(int): the first integer
        b(int): the second integer

    Return:
        the sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
