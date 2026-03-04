#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for i in range(len(row)):
            # Print the integer
            print("{:d}".format(row[i]), end="")
            # Only print a space if it's NOT the last element in the row
            if i < len(row) - 1:
                print(" ", end="")
        # Print a newline after each row
        print()
