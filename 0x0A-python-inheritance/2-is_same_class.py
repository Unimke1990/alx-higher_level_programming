#!/usr/bin/python3
"""check for an object instance of a class"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
