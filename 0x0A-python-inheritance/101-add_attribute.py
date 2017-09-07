#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """Defines function to check whether object supports dynamic assigment.

    Args:
        obj: object to check/assign to
        attr (str): name of attribute to assign to `obj`
        value: value to be associated with `name`

    Raises:
        TypeError: If `obj` does not support dynamic assignment
    """
    if not isinstance(attr, str) or \
       hasattr(obj, attr) or not\
       hasattr(obj, "__setattr__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
