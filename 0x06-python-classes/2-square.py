#!/usr/bin/python3
"""writing a class square
"""


class Square:
    """class defined by private instance attribute
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
