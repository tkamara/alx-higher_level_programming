#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    num = count - 1
    while num >= 0:
        print("{:d}".format(my_list[num]))
        num -= 1
