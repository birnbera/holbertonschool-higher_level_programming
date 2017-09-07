#!/usr/bin/python3
"""Module implementing Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class to represent a Square as a subclass of Rectangle"""
    def __init__(self, size):
        """Initialize new Square object

        Args:
            size (int): side lengths
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute area of square"""
        return self.__size**2

    def __str__(self):
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size, self.__size)
