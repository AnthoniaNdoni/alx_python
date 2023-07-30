#!/usr/bin/env python3
def fibonacci_sequence(n):
    sequence = [0,1]
    if n == 0:
        sequence = []
    if n == 1:
        sequence = [0]
    while Len(sequence)<n:
        adder = sequence[-1] + sequence[-2]
        return sequence