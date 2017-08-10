#!/usr/bin/python3


def best_score(my_dict):
    if my_dict:
        return max(my_dict.items(), key=lambda x: x[1])[0]
    return None
