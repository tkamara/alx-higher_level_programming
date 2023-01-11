#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        calculates area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Arguments:
            name(str): a name
            value: the int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
