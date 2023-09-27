#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """method takes an optional size parameter with a default value of 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The method returns the computed area"""
        return self.__size ** 2
