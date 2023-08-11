#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    def is_same_class(obj, a_class):
    Check if a object is an instance of a specified class .

    Args:
    obj: The object to be checked.
    a_class: The  specified class .

    Returns: True if the object is an instance of  the  specified  class , otherwise False.
    """
    return isinstance(obj, a_class)
