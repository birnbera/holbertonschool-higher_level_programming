#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius=0):
        """Initialize circle with default radius=0

        __init__ method initializes radius and test if numeric"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate area of circle based on radius"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference with given radius"""
        return 2 * math.pi * self._MagicClass__radius

import dis

dis.dis(MagicClass)
