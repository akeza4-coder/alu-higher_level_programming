#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, area, and perimeter.
"""


class Rectangle:
    """Defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Retrieves the width."""
=======
        """Retrieves the private width attribute."""
>>>>>>> f764066cd66543ebb0c1b6b0ddcbda1f5a4271ab
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
<<<<<<< HEAD
        """Retrieves the height."""
=======
        """Retrieves the private height attribute."""
>>>>>>> f764066cd66543ebb0c1b6b0ddcbda1f5a4271ab
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
<<<<<<< HEAD
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
=======
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle perimeter.
        Returns 0 if width or height is 0.
        """
>>>>>>> f764066cd66543ebb0c1b6b0ddcbda1f5a4271ab
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
