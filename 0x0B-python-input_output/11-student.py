#!/usr/bin/python3
"""Module implementing class with method to serialize itself"""


class Student:
    """Class to represent student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new student instance with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Create copy of attributes for use in json string"""
        return self.__dict__.copy()
