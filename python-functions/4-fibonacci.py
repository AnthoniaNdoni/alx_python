#!/usr/bin/env python3
def fibonacci_sequence(n):
    sequence = [0, 1]
    if n <= 0:
        sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
        return sequence
    

    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
