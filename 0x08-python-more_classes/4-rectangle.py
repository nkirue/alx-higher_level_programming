#!/usr/bin/python3
""" a class Rectangle that defines a rectangle."""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        """It initialize a new Rectangle with width and height  """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area """
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This method returns the printable representat."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for i in range(self.__height):
            [rectan.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """This method returns the string representat."""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)
