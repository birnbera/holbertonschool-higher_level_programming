#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0.
    numer = sum(map(lambda x: x[0] * x[1], my_list))
    denom = sum(map(lambda x: x[1], my_list))
    return numer/denom
