#!/usr/bin/python3
"""
    Rectangle that inherits from BaseGeometry (5-base_geometry.py)
    """
class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.
    """
def __init__(self, width, height):
    """
    Initializes a new Rectangle instance with the specified width and height.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height

def area(self):
    """
    Calculates and returns the area of the rectangle.

    Returns: The area of the rectangle.
    """
    return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:A string in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
