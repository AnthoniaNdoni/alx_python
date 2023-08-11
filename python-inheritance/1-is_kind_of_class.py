#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    This function compares the type of the given object (obj) with the
    specified class (a_class) and returns True if they match exactly,
    indicating that the object is an instance of the specified class.
    Otherwise, it returns False.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class