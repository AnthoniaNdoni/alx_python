#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

if __name__ == "__main__":
    r = Rectangle(3, 4)
    print(r)
    print(dir(r))