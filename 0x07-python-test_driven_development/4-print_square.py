#!/usr/bin/python3
"""
Function that prints a square
"""


def print_square(size):
    """
    Printing a square using #

    Parameters:
    size(int): size length of square

    Return:
    print the square according to length
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
