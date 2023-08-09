#!/usr/bin/python3
"""
Module Documentation - Square Class

This module contains the definition of the Square class.
"""

class Square:
    """
    Represents a square with a given size.
    
    Attributes:
        __size (int): The size of the square.
        
    Methods:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the specified size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """Get the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()
