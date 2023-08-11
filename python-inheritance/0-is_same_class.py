#!/usr/bin/python3
"""
    def is_same_class(obj, a_class):
    Check if an object is an instance of or inherited from a specified class.

    Args:
    obj: The object to be checked.
    a_class: The specified class.

    Returns: True if object is an instance of the specified class, otherwise False.
    """
def is_same_class(obj, a_class):
    """
    def is_same_class(obj, a_class):
    check if an object is an instance of a specified class

    Args:
    obj: The object to be checked.
    a_class: The specified class.

     Returns: True if object is an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class