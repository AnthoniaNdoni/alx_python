#!/usr/bin/env python3
def pow(a, b):
    mul = 1
    for _ in range(b):
        mul = mul * a
    return mul
