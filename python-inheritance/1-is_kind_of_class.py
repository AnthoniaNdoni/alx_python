#!/usr/bin/python3
"""
    def is_kind_of_class(obj, a_class):
    Defines a function is_kind_of_class that checks if an object is an instance
    of a specified class or a class that inherits from it.

    Args:
    obj: The object to be checked.
    a_class: The class to compare against.
    True if obj is an instance of a_class or its subclass, otherwise False.
    """

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it's an instance of a class
    that inherits from, the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)