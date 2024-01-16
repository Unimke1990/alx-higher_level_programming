#!/usr/bin/python3
"""check for an object instance of a class"""


def is_same_class(obj, a_class):
    """returns True if object and
    False id not object """
    return type(obj) == a_class
