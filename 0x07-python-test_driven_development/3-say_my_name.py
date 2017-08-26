#!/usr/bin/python3
"""Module containin function to print name.

To be used as a module. Contains no directly executable code.
"""


def say_my_name(first_name, last_name=""):
    """Function that prints a name

    Args:
        first_name (str): First name to print
        last_name (str): Last name to print

    Returns: None

    Raises:
        TypeError: If `first_name` or `last_name` are not strings.
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
