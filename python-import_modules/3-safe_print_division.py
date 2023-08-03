#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = "None"
        return result
    finally:
        print("inside result: {}".format(result))
        

# test the function
result = safe_print_division(10, 2)   