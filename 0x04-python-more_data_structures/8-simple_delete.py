#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    if not my_dict is None:
        my_dict.pop(key, None)
    return my_dict
