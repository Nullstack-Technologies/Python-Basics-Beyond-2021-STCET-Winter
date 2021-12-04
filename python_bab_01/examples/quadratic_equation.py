"""
    Program to Compute the Roots of a Quadratic Equation
    Author:
    Date:

    input -> a, b and c

    ax^2 + bx + c = 0
    discriminant = b^2 - 4*a*c
    (-b +- sqrt(discriminant)) / 2*a
"""
import math



print("Program to Compute the Quadratic Roots of a Quadratic Equation:")
print("ax^2 + bx + c = 0, we are to find x1 and x2(roots of the equation)")
print("Please provide the values of a, b and c:")
print("")

a = int(input("Please input 'a': "))
b = int(input("Please input 'b': "))
c = int(input("Please input 'c': "))


print("Finding the roots of the equation {}x^2 + {}x + {}".format(a, b, c))
print("....")

discriminant = b ** 2 - 4 * a * c
discriminant = math.sqrt(discriminant)

x1 = (-b + discriminant) / 2 * a
x2 = (-b - discriminant) / 2 * a


print("The roots of the equation are: {}, {}".format(x1, x2))





