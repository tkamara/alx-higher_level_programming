#!/usr/bin/python3
"""
function checking if exact same object
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
