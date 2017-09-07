#!/usr/bin/python3
"""Module implementing BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def __init__(self):
        """Initialize new instance of BaseGeometry"""
        pass

    def area(self):
        """Compute area of self"""
        raise Exception('area() is not implemented')
