#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is None:
        set_1 = set()
    if set_2 is None:
        set_2 = set()
    return set_1 ^ set_2
