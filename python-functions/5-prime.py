#!/usr/bin/env python3
def is_prime(number):
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    for i in range(2, int(number ** 0.5) +1):
        if number % i == 0:
            return False
        
    return True
    result = is_prime(17)
    print(result)

    result = is_prime(4)
    print(result)