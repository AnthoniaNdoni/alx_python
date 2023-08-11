#!/usr/bin/python3
"""
    BaseGeometry = __import__('7-base_geometry').BaseGeometry
    class Rectangle(BaseGeometry):
    def __init__(self, width, height):
    Defines a class Rectangle that inherits from BaseGeometry
    Initializes a new Rectangle instance with the specified width and height.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
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

    Returns:None
    """
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height 