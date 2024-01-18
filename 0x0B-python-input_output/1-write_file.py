#!/usr/bin/python3
"""define a function that reads files to stdout"""


def write_file(filename="", text=""):
    """write to the file"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
