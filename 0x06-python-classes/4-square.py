#!/usr/bin/python3
"""This defines a class Square"""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """method takes an optional size parameter with a default value of 0"""
        self.size = size

    @property
    def size(self):
        """Get/set methods defined using the @property and @size.setter decor"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The method returns the computed area"""
        return self.__size ** 2
