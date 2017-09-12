#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        setattr(self, "width", value)

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.x, self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        attrs = ["id", "size", "x", "y"]
        for i, arg in enumerate(args[:len(attrs)]):
            setattr(self, attrs[i], arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
