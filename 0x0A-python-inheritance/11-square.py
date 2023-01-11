#!/usr/bin/python3
"""
class inheriting from other class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class inheriting from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        area of square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        str method
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
