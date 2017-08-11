#!/usr/bin/python3


def complex_delete(my_dict, value):
    if my_dict:
        to_del = []
        for k, v in my_dict.items():
            if v is value:
                to_del.append(k)
        for k in to_del:
            del(my_dict[k])
    return my_dict
