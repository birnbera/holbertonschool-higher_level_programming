#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    if my_dict is not None:
        my_dict.pop(key, None)
    return my_dict
