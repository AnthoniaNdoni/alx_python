#!/usr/bin/python3
"""
    Module that defines a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the specified width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Returns:
        None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Generates the string representation of the rectangle.

        Returns:
        str: The formatted string representing the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)