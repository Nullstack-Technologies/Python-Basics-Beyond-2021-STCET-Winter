"""
    Find The Factorial of a number using Functions
"""


def fact(n):
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



# Taking Input from users
n = float(input("Please provide the n:"))
r = float(input("Please provide the r:"))

# calculate nPr
permutation = fact(n) / fact(n-r)

# calculate nCr
combination = fact(n) / (fact(n-r) * fact(r))

print(f"Permutation is: {permutation}")
print(f"Combination is: {combination}")