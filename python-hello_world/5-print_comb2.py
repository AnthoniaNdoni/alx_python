#!/usr/bin/python3
for num in range(0, 100):
    if num <= 9:
        print("0{}".format(num), end=", ")
    else:
        print("{}, ".format(num) if num < 99 else "{}".format(num), end=" ") 
