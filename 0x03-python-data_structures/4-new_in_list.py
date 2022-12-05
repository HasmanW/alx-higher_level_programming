#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        my_list_copy = [value for value in my_list]
        my_list_copy[idx] = element
        return my_list_copy
