def is_same_class(obj, a_class):
    return type(obj) is a_class

<<<<<<< HEAD
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__), end="")
=======
    Args:
    obj: The object to be checked.
    a_class: The  specified class .

    Returns: True if the object is an instance of  the  specified  class , otherwise False.
    """
    return type(obj) is a_class
>>>>>>> bf799d92a1b48d312f3593a9676dd2e36d4af381
