#!/usr/bin/python3
"""Module defining function to test class membership"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance and not a subclass of a_class"""
    return type(obj) is a_class
