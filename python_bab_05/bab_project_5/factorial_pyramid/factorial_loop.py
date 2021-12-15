"""
    Factorial using Loop
"""

from .lib import time_it


@time_it
def factorial_2(n):
    """
        Computes the Factorial of a number n
        n! = n * (n-1) * (n-2)* .... 1
        input: n
        output: factorial of a number
    """

    fact_output = 1
    while n > 1:
        fact_output *= n
        n -= 1
    return fact_output


@time_it
def factorial_3(n):
    """
        Computes the Factorial of a number n
        n! = n * (n-1) * (n-2)* .... 1
        input: n
        output: factorial of a number
    """

    fact_output = 1
    for x in range(2, n + 1):
        fact_output *= x
    return fact_output
