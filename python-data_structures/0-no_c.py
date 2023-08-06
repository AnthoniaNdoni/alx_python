#!/usr/bin/env python3
def no_c(my_string):
    return ''.join(char for char in my_string if char.lower() not in ('c', 'Ç'))

original_string = "Holberton school!"
result = no_c(original_string)
print(result)