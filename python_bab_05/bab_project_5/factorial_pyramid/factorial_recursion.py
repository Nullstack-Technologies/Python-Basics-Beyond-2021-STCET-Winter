"""
    Factorial using Recursion
"""

from .lib import time_it


@time_it
def factorial_1(n):
    """
        Computes the Factorial of a number n
        n! = n * (n-1) * (n-2)* .... 1
        input: n
        output: factorial of a number
    """
    # termination
    if n == 1:
        return 1
    # recursive calls
    else:
        return n * factorial_1(n-1)
