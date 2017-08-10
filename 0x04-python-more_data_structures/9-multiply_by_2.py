#!/usr/bin/python3


def multiply_by_2(my_dict):
    new_dict = {}
    if my_dict is not None:
        for k in my_dict.keys():
            new_dict[k] = my_dict[k] * 2
    return new_dict
