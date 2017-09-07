#!/usr/bin/python3
"""Module implementing function to look up attributes of object"""


def lookup(obj):
    """Return list of attributes and methods of obj"""
    return dir(obj)
