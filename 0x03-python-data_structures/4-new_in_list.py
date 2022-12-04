#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    count = len(copy)
    if idx < 0 or idx >= count:
        return copy
    else:
        copy[idx] = element
        return copy
