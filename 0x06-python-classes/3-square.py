#!/usr/bin/python3
"""writing a class Square that defines a square
"""


class Square:
    """defining the class by private instance attribute size
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """defining the class by public instance method
    """
    def area(self):
        area = self.__size * self.__size
        return area
