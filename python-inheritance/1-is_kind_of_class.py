#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of or inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or inherited from it, False otherwise.
    """
    return isinstance(obj, a_class)