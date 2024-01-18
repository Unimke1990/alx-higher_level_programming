#!/usr/bin/python3
"""define a function that reads files to stdout"""


def read_file(filename=""):
    """print the file's content"""
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
