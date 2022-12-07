#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for ref in new:
        print("{}: {}".format(ref, a_dictionary[ref]))
