#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is not None:
        return list(map(lambda x: replace if x == search else x, my_list))
