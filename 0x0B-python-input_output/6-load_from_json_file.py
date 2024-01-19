#!/usr/bin/python3
"""define a function that reads from a json file"""
import json


def load_from_json_file(filename):
    """create a python object from a json file"""
    with open(filename, "r") as filename:
        return json.load(filename)
