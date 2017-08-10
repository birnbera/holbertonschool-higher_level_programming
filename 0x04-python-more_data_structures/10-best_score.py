#!/usr/bin/python3


def best_score(my_dict):
    if my_dict is not None:
        return max(my_dict.items(), default=None, key=lambda x: x[1])[0]
    return None
