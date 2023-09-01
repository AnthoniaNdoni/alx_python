#!/usr/bin/python3
"""
    class BaseGeometry:
    An empty class representing BaseGeometry.
     Raises an Exception with the message area() is not implemented.

    Args:
    self: The object itself.
    """
class BaseGeometry:
    """
    An empty class representing BaseGeometry.
    Raises an Exception with the message area() is not implemented.
    Args:
    self: The object itself.
    """

def area(self):

    def __dir__(cls) -> None:
        """
        The function overide the default __dir__ function    
        """
        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri

    def area(self):
        """
        This function raise an error if the area method is not define
        """
        raise Exception("area() is not implemented")