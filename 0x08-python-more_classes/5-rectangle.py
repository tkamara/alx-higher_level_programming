#!/usr/bin/python3
"""
defining class Rectangle
"""


class Rectangle:
    """class having private instances width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """defining public instances
    """
    def area(self):
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        perimeter = (2 * self.__width) + (2 * self.__height)
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (perimeter)

    def print_rect(self):
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "#"
            if row < (self.__height - 1) and self.__width != 0:
                str += "\n"
        return str

    def __str__(self):
        return self.print_rect()

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
