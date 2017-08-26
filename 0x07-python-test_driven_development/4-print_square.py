#!/usr/bin/python3
"""Module containing function to print a square

Should not be executed directly, but only imported as a module
"""


def print_square(size):
    """Function to print a square with sides `size`.

    Args:
        size (int): Integral side length of square

    Returns: None

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """
    if type(size) is not float and type(size) is not int:
        raise TypeError('size must be an integer')
    if type(size) is float and size != round(size):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(round(size)):
        print("#" * round(size))
