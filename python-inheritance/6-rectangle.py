#!/usr/bin/python3
"""
    class Rectangle(BaseGeometry):
    this module Defines a class Rectangle that inherits from BaseGeometry
    """
class Rectangle(BaseGeometry):
    """
   `Am empty class representing Rectangle
    Initializes a new Rectangle instance with the specified width and height.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Returns:None
    """

def __init__(self, width, height):
    """
    def __init__(self, width, height):
    initializes a function that inherits a class properties
    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Returns:None
    """
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height 
