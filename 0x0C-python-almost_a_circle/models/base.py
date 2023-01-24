#!/usr/bin/python3
"""
creating class Base
"""
import json


class Base:
    """
    the base of other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialising

        Arguments:
            id(int): identity of new base
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes to JSON string rep to file

        Arguments:
            list_objs: list of instances who inherits of Base
        """
        if list_objs is None:
            new = []
        else:
            new = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """returns list from JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return json.loads([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes set

        Arguments:
            **dictionary: kwargs
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as new_file:
                new_list = Base.from_json_string(new_file.read())
                return [cls.create(**i) for i in new_list]
        except IOError:
            return []
