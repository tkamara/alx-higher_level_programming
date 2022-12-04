#!/usr/bin/python3
def print_list_integer(my_list=[]):
    num = 0
    count = len(my_list)
    while num < count:
        print("{:d}".format(my_list[num]))
        num += 1
