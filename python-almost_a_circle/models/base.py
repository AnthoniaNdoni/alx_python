#!/usr/bin/python3
"""
module documentation: 
"""

class Base:
    """
    Base class for managing the id attribute in all future classes.
    Attributes:
        __nb_object (int): A private class attribute that keeps track of the number of instances created.
        id (int): A public instance attribute representing the unique identifier of an instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor.

        Args:
        id (int, optional): The id for the instance.Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects