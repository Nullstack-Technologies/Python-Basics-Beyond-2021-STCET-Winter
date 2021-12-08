"""
    Find The Factorial of a number using Functions
"""


def fact_recur(n):
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
        return n * fact_recur(n-1)


# Taking Input from users
n = float(input("Please provide the n:"))
r = float(input("Please provide the r:"))

# calculate nPr
permutation = fact_recur(n) / fact_recur(n-r)

# calculate nCr
combination = fact_recur(n) / (fact_recur(n-r) * fact_recur(r))

print(f"Permutation is: {permutation}")
print(f"Combination is: {combination}")
