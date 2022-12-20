#!/usr/bin/python3
"""writing a class square that defines a square
"""


class Square:
    """the class

    Args:
        size (int): the length of one side of the square

    Attributes:
        __size (int): the length of one side of the square

    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """defining class by public instance method
    """
    def area(self):
        area = self.__size * self.__size
        return area
