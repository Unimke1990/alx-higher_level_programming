#!/usr/bin/python3
"""define a lookup method"""


def lookup(obj):
    """retuns a list of obj methods and attributes"""
    return (dir(obj))
