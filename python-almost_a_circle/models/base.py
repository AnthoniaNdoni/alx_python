"""
module documentation: 
"""

class Base:
    """
    Base class for managing the id attribute in all future classes.
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        class constructor.

        Args:
        id (int, optional): The id for the instance.Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects