#!/usr/bin/python3
"""
    BaseGeometry Module
    """

class BaseGeometryMetaClass(type):
    """
    An metaclass for Base Geometry.
    """
    def __dir__(cls)->None:
        """
        A function define to remove the __init_subclass__ from dir
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    this method check if a class is an instance of the define object
    exam 1 is an instancce of the class int
    """

    def __dir__(cls) -> None:

        attrib = super().__dir__()
        n_attri = []
        for attr in attrib:
            if attr != '__init_subclass__':
                n_attri.append(attr)
        return n_attri