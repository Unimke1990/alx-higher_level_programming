#!/usr/bin/python3
"""define a function that converts str to json"""
import json


def to_json_string(my_obj):
    """return the json representation of the str"""
    return json.dumps(my_obj)
