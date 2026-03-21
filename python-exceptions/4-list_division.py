#!/usr/bin/python3
"""
Module for dividing elements of two lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.
    Returns: A new list (length list_length) with all divisions.
    """
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)
    return (new_list)
