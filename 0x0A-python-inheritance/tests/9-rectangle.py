#!usr/bin/python3
"""Defines a class Rectangle that
inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)/
