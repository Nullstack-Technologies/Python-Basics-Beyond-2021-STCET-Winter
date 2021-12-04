"""
    Factorial Using Loops
    n * (n-1)* ... 1
"""

n = int(input("Please provide the number you want to find factorial of:"))


fact = 1
# using while
while n > 1:
    fact *= n
    n -= 1

# using for
for x in range(2, n + 1):
    fact *= x

# i = 0
# while i >= len(range(2, n + 1)):
#     fact *= n
#     n -= 1
#     i += 1



print(f"The Factorial is: {fact}")



