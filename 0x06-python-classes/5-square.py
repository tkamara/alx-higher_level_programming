#!/usr/bin/python3
"""writing a class that prints a square
"""


class Square:
    """class Square

    Args:
        size (int): length of one side of the square

    Attributes:
        __size (int): length of one side of the square

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

    """defining a public instance method
    """
    def area(self):
        area = self.__size * self.__size
        return (area)

    """defining a public instance method
    """
    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
