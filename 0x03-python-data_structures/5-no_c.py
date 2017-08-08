#!/usr/bin/python3


def no_c(my_string):
    new_string = [c for c in my_string if (c is not "c" and c is not "C")]
    return "".join(new_string)
