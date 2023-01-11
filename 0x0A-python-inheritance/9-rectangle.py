#!/usr/bin/python3
"""
class inheriting from other class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str method for rectangle
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
