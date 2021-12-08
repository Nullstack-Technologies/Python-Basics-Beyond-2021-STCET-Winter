import math

"""
    Program to Compute the Permutation and Combination
    Author:
    Date:

    # Arrangements/ Permutation 
    nPr = n!/(n-r)!
    8 pens of diff colour and how many arrangements of 4 can you make
    RB ~= BR
    8Pr


    # Combination
    nCr = n!/(n-r)!*r!
    8 teams in IPL
    8C2
    KKR vs CSK
    CSK vs KKR


"""

# Taking Input from users
n = float(input("Please provide the n:"))
r = float(input("Please provide the r:"))

# calculate nPr
permutation = math.factorial(n) / math.factorial(n-r)

# calculate nCr
combination = math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

print(f"Permutation is: {permutation}")
print(f"Combination is: {combination}")

