#!/usr/bin/python3
"""
function checking if exact same object
"""


def is_same_class(obj, a_class):
    """
    checking if obj is exactly an instance of class
    Arguments:
        obj: the object
        a_class: the class
    """

    if type(obj) == a_class:
        return True
    else:
        return False
