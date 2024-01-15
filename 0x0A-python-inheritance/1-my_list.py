#!/usr/bin/python3
"""defining a Mylist class that inherits from list"""


class MyList(list):
    """defining a method that prints the list"""

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
