#!/usr/bin/python3
def no_c(my_string):
    my_string_copy = [value for value in my_string if value != 'c' and value != 'C']
    return ("".join(my_string_copy))
