#!/usr/bin/python3
"""
class that inherits from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class inheriting from Rectangle
    """
    def __init__(self, size):
        """
        method defining square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        the area of square
        """
        return self.__size * self.__size
