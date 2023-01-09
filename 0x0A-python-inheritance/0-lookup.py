#!/usr/bin/python3
"""
Function to return list of attribute and methods
"""


def lookup(obj):
    """
    Returns available attributes and methods of an object

    Arguments:
        obj: the object

    Return:
        list object
    """
    return (dir(obj))
