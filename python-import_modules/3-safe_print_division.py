#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("cannot divide by zero.")
        return None
    else:
        print("insiden result: {}".format(result))
        print("{} / {} = {}".format(a, b, result))
        return result
    finally:
        print()

# test the function
result = safe_print_division(10, 2)   