#!/usr/bin/python3
"""define a function that converts json to str"""
import json


def from_json_string(my_str):
    """return the str representation of the json"""
    return json.loads(my_str)
