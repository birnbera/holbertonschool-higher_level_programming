#!/usr/bin/python3
"""Module containing simple function to add together two integers

Must import this module to use it. Cannot be executed directly.
To run doctests:
    $ python3 -m doctest -v ./tests/0-add_integer.txt
"""


def add_integer(a, b):
    """Add two integers

    Args:
        a: First integer to add. If type(a) is float, it is first
            casted to an int.
        b: Second integer to add. If type(b) is float, it is first
            casted to an int.

    Returns:
        Sum of `a` and `b`

    Raises:
        TypeError: If `type(a)` or `type(b)` is neither an int nor
        float.
"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    result = a + b
    if result != result or result == float('inf') or result == -float('inf'):
        raise OverflowError
    return int(a) + int(b)
