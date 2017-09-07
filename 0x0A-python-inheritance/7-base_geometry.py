#!/usr/bin/python3
"""Module implementing BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class to extend"""
    def area(self):
        """Function to compute area of self"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function to validate value is an int"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
