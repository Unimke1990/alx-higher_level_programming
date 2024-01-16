#!/usr/bin/python3
"""check for an object instance of a class"""


def inherits_from(obj, a_class):
    """
    returns:
    True if obj is an instance
    False if otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
