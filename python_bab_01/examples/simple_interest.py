"""
    Program to Compute the Simple Interest
    Author:
    Date:
"""

# Taking Input from users
principal = float(input("Please provide the Principal:"))
rate_of_interest = float(input("Please provide the Rate of Interest:"))
no_of_years = float(input("Please provide the time in years:"))

# simple_interest_1 = principal * rate_of_interest * no_of_years / 100
simple_interest = (principal * rate_of_interest * no_of_years) / 100

print(f"the Simple Interest is {simple_interest}")
print(f"the Amount is {simple_interest + principal}")

