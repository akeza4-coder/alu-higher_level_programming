#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples using only the first two elements of each."""
    # Ensure tuple_a has at least 2 elements by adding (0, 0)
    # If it's longer, we only take the first two: [:2]
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]

    return (a[0] + b[0], a[1] + b[1])
