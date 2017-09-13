#!/usr/bin/python3
"""Module to represent Base object to be extended by Square and Rectangle"""
import json


class Base:
    """Base class to be subclassed by Square and Rectangle"""

    __nb_object = 0
    """Class variable representing the total count of Base (and subclass)
    instances.
    """

    def __init__(self, id=None):
        """Initialize new Base instance

        Args:
            id: Identifier for instance. If None, use current object count.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_object += 1
            self.id = type(self).__nb_object

    @classmethod
    def create(cls, **dictionary):
        """Method to create new instance directly from the class. Mainly
        for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for new instance.

        Returns: New instance of class from which `create` was called.

        Raises: Errors delegated to subclasses of Base which call this
            method.
        """
        c = cls(1, 1)
        if type(dictionary) is not dict:
            dictionary = {}
        c.update(**dictionary)
        return c

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to serialize list of dictionary objects into json.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into json
                representation.

        Returns: Json string representation of `list_dictionaries`.

        Raises: Any errors encounterd during serialization.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static method to deserialize json string into python objects.

        Args:
            json_string (str): String representation of objects.

        Returns: Python objects represented by `json_string`.

        Raises: Any errors encountered during serialization.
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to convert `list_objs` to json string and
        save in file with name '<class name>.json'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any errors encountered during serialization and I/O.
        """
        if not list_objs:
            list_objs = []
        with open("{}.json".format(cls.__name__), 'w') as jf:
            jf.write(cls.to_json_string([obj.to_dictionary() for
                                         obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Class method to load file containing json serialized objects.
        Attempts to open file named '<class name>.json' and deserialize
        it. If it does not exist, returns empty list.
        """
        try:
            with open("{:s}.json".format(cls.__name__), 'r') as jf:
                list_dictionaries = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dictionaries]
        except:
            return []
