#!/usr/bin/python3
"""
only sub class of
"""


def inherits_from(obj, a_class):
    """
    check if obj is an instance of class inherited from specified class
    Arguments:
        obj: the object
        a_class: the specified class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
