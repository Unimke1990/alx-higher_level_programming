#!/usr/bin/python3

"""define a class Square."""


class Square:
    """A class Square with private attribute"""

    def __init__(self, size):
        """initializes a square with the size given.

        Args:
            size (int) : The size of the new square
        """
        self.__size = size
