"""
module documentation
"""
from models.rectangle import Rectangle 

class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    
    Attributes:
        size (int): The size of the square (same as width and height).
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The unique identifier of the instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            size (int): The size of the square (same as width and height).
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)  # Call the constructor of the Rectangle class
        self.size = size

    # Additional methods, if needed...

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)