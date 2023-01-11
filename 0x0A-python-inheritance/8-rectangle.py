#!/usr/bin/python3
"""
creating class that inherits from other class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        function that defines rectangle width and height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
