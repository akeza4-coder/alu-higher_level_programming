#!/usr/bin/python3
"""
Module for safe integer division with debug message.
"""


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result in a finally block.
    Returns: The value of the division, otherwise: None.
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return (result)
