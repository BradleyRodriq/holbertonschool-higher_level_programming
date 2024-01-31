#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except TypeError:
        result = None
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside Result: {}".format(result))
    return(result)
