#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        k = 1
        for b in a:
            if k == len(a):
                print("{:d}".format(k), end="")
            else:
                print("{:d}".format(k), end=" ")
            k = k + 1
        print()
