#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original."""
    # Create a copy of the list first
    copy = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return copy

    copy[idx] = element
    return copy
