#!/usr/bin/python3
"""check for an object instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    returns:
    True if obj is an instance
    False if otherwise
    """
    return isinstance(obj, a_class)
