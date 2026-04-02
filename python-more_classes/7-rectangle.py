#!/usr/bin/python3
"""
This module defines a Rectangle class with a customizable print symbol.
"""


class Rectangle:
    """Defines a rectangle by width, height and tracks instances/symbols."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle and increments instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the private width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter (0 if width or height is 0)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation of the rectangle.
        Uses the character(s) stored in print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Format rows carefully to avoid PEP8 line length errors
        res = ""
        for i in range(self.__height):
            res += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                res += "\n"
        return res

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message and decrements instance count on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
