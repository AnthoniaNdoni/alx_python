#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

square1 = Square('0-square')
square2 = Square(3)

print(type(square1))
print(square2.__dict__)
