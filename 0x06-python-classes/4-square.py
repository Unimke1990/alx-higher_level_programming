#!/usr/bin/python3

"""define a class Square."""


class Square:
    """A class Square with private attribute"""

    def __init__(self, size=0):
        """initialize a new square

          Args:
            size (int) : value to be added
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """cal and return the area of the square"""
        return self.__size ** 2
