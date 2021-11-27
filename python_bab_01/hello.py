# Here we print a Hello Dog!
# ctrl + / will comment a line
print("Hello 🐶!")
print("Ok Ok Ok ")

# Inputs in Python
# coming out of the input -> ctrl + c
name = input("Whats Your Name?:")
age = input("Whats Your Age?:")
print(f"Hey {name}!, your Age is {age} and thats cool!🐶")
print("Hey %s!, your Age is %s and thats cool!🐶" %(name, age))
print("Hey {}!, your Age is {} and thats cool!🐶".format(name, age))


# Basic Data Types of Python
name = "Nauman Arif"      # string
age = 100                 # int
height = 120.05           # float
is_married = True         # boolean

# printing the variables
print(name)
print(age)
print(height)
print(is_married)
print(f"Hey {name}, your age is {age} and you are {height} cms? You are also married ? {is_married}")

# print the types of the variables
print(type(name)) # string
print(type(age))  # int
print(type(height)) # float
print(type(is_married)) # bool


# Type Casting
# int(), str(), float(), bool()
name = input("Please give your name?:")
age = input("Please provide your age?:")
height = input("Please give your height?:")
is_married = input("Are You Married?:")

age = int(age)
height = float(height)
is_married = bool(is_married)


print(f"Hey {name}, your age is {age} and you are {height} cms? You are also married ? {is_married}")


