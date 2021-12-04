"""
    Program to Compute the Area of a Triangle
    Author:
    Date:

    input -> b and h
    1/2 * b * h
"""

print("Program to Compute the Area of a triangle:")
print("Given the lengths of height(h) and base(b) of a triangle, we compute the area:")
print("Please provide the values of b and h:")
print("")

b = float(input("Please input Base 'b': "))
h = float(input("Please input Height 'h': "))


print("Finding the area of the given traingle")
print("....")

# computing the area of the triangle
area = 0.5 * b * h

print("The are of the Triangle is: {}".format(area))
