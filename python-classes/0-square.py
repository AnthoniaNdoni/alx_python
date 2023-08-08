#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

square1 = Square()
square2 = Square(3)


print(square2.__dict__)  