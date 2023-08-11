def is_same_class(obj, a_class):
    return type(obj) is a_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__), end="")