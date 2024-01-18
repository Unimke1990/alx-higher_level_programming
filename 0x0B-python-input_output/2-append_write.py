#!/usr/bin/python3
"""define a function that reads files to stdout"""


def append_write(filename="", text=""):
    """write to the file"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
