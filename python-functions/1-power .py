#!/usr/bin/python3
def pow(a, b):
     if b  == 0:
          return 1
     result = a
     for _ in range(1, b):
          result *= a

     return result

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))