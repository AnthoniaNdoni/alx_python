#!/usr/bin/python3
"""
Square Module

This module defines the Square class, which represents a square with a given size.
The class provides methods to interact with and manipulate square objects.

Classes:
    Square

Methods:
    __init__(self, size)
    area(self)
"""

class Square:
    """
    Represents a square with a given size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the specified size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
    
    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
