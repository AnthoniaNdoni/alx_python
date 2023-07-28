#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        mul = 1
        for _ in range(b):
            mul = mul * a
        return result
    else:
        return 1 / pow(a, -b)
