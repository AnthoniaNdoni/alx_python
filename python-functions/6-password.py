#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        if not (has_uppercase and has_uppercase and has_digit):        
         return False
    if ' ' in password:
         return False
    
    return True

result = validate_password("Abcdefg123")
print(result)

result = validate_password("password123")
print(result)

result = validate_password("Password with space")
print(result) 