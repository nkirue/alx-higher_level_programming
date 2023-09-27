#!/usr/bin/python3
"""This defines a class Square"""


class Square:
    """This represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """method takes size parameter with a default value of 0
           and position with (0, 0) of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set methods defined with the @property and @size.setter deco"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set method of the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """The method returns the computed area."""
        return self.__size ** 2

    def my_print(self):
        """method is defined as a public"""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
