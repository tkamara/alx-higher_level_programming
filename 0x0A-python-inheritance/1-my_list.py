#!/usr/bin/python3
"""
class that inherites
"""


class MyList(list):
    """
    the class that inherits from list
    """
    def print_sorted(self):
        """
        method to sort the list
        """
        print(sorted(self))
