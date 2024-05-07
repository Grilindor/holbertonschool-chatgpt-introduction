#!/usr/bin/python3

import sys

# Function Description:
# This function calculates the factorial of a given number using recursion.

def factorial(n):
    # Parameters:
    # n: An integer for which the factorial needs to be calculated.

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        #Return:
        #int: the factorial of the input integer.

f = factorial(int(sys.argv[1]))
print(f)
