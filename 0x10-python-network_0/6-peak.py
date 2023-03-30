#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    It finds and returns thepeak in a list of integers
    Using recursion
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if (size == 1):
        return list_of_integers[0]
    if (size == 2):
        return max(list_of_integers)

    middle = int(size / 2)
    res = list_of_integers[middle]
    if res > list_of_integers[middle - 1] and res > list_of_integers[middle + 1]:
        return res
    elif res < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
