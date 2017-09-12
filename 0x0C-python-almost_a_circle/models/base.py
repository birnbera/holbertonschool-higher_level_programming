#!/usr/bin/python3
import json


class Base:
    __nb_object = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_object += 1
            self.id = type(self).__nb_object

    @classmethod
    def create(cls, **dictionary):
        c = cls(1, 1)
        c.update(**dictionary)
        return c

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string == "" or type(json_string) is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{:s}.json".format(cls.__name__), 'w') as jf:
            jf.write(cls.to_json_string([obj.to_dictionary() for
                                         obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        try:
            with open("{:s}.json".format(cls.__name__), 'r') as jf:
                list_dictionaries = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dictionaries]
        except:
            return []
