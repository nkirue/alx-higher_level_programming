#!/usr/bin/python3
"""This defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes a new Rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter."""
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
        """Getter/setter."""
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
        """the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """the Rectangle with the greater"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Square"""
        return (cls(size, size))

    def __str__(self):
        """This method returns the printable representat"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rtan = []
        for i in range(self.__height):
            [rtan.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rtan.append("\n")
        return ("".join(rtan))

    def __repr__(self):
        """the string representation"""
        rtan = "Rectangle(" + str(self.__width)
        rtan += ", " + str(self.__height) + ")"
        return (rtan)

    def __del__(self):
        """a message for every deletion """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
