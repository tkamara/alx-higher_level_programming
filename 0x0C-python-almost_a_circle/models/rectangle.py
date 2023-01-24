#!/usr/bin/python3
"""
class that inherits from base
"""
from models.base import Base

class Rectangle(Base):
    """
    defining Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialising a new rectangle

        Arguments:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): the x coordinate
            y(int): the y coordinate
            id(int): the identity of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        get width of rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        get height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def x(self):
        """get the x coordinate
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get the y coordinate
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        obtaining area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ displaying the rectangle
        """
        str=""
        if self.__height != 0 and self.__width != 0:
            str += ("\n" * self.__y)
            for num in range(self.__height):
                str += (" " * self.__x)
                str += ("#" * self.__width)
                if num != self.__height - 1:
                    str += "\n"
        print(str)

    def update(self, *args, **kwargs):
        """assigning arguments to each attribute
        """
        if len(args) != 0:
            for num,arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.__width = arg
                elif num == 2:
                    self.__height = arg
                elif num == 3:
                    self.__x = arg
                elif num == 4:
                    self.__y = arg

        else:
            for key,value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dict representation of rectangle
        """
        to_dict = { "id" : self.id, "width" : self.__width, "height" : self.__height, "x" : self.__x, "y" : self.__y}
        return to_dict


    def __str__(self):
        """string representation
        """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)
