#!/usr/bin/python3

"""define a class Square."""


class Square:
    """A class Square with private attribute"""

    def __init__(self, size=0):
        """initialize a new square

          Args:
            size (int) : value to be added
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """cal and return the area of the square"""
        return self.__size ** 2
