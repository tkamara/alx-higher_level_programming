#!/usr/bin/python3
"""
came class or inherit /from
"""


def is_kind_of_class(obj, a_class):
    """
    function that checks if obj is insrance of
    Arguments:
        obj: the object
        a_class: the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
