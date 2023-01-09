#!/usr/bin/python3
"""
class that inherites from another class
"""


class MyList(list):
    pass

    def print_sorted(self):
        """
        method to sort the list
        """
        print(sorted(list(self)))
