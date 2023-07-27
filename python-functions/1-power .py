#!/usr/bin/env python3
def pow(a, b):
    while b != 0:
        a = a * a
        b = b - 1
    return a
