#!/usr/bin/python3
"""define a function that writes to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """creating the json file"""
    with open(filename, "w") as filename:
        json.dump(my_obj, filename)
