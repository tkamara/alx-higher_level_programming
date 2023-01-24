#!/usr/bin/python3
"""
The class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    defining the sqaure
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialising the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getting square size
        """
        return self.width
    
    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dict representaiton of square
        """
        to_dict = {"id" : self.id, "size" : self.size, "x" : self.x, "y" : self.y}
        return to_dict

    def __str__(self):
        """string representation
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.size)
