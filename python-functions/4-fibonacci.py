#!/usr/bin/env python3
def fibonacci_sequence(n):
    sequence = [0, 1]
    if n <= 0:
        sequence = []
    if n == 1:
        sequence = [0]
    else:
        while len(sequence) < n:
            added = sequence[-1] + sequence[-2]
            sequence.append(added)
    return sequence
