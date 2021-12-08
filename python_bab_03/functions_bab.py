"""
    Functions in Python
"""


# A function is a block of code that executes only when it is called

# definition
def greet_me():
    print("Hey, This is Python Basics & Beyond!")

# calling
greet_me()


# paramters /arguments
def greet_me(name):
    print(f"Hey {name}, This is Python Basics & Beyond!")


greet_me("Nauman")


# DRY -> Don't Repeat Yourself
# Divide & Conquer -> 


# default values in parameters
def greet_me(first_name="Nauman", last_name="Arif"):
    """
        This Function is greeting me with my name
        Input:
        Output:
    """
    print(f"Hey {first_name} {last_name}, This is Python Basics & Beyond!")
    #return None

greet_me('Nauman')
greet_me('Nauman')
greet_me(last_name='Nauman')



# Function Return Values
def add(x, y):
    """
        Add Two Numbers
    """
    sum = x + y
    return sum

sum = add(1,2)
print(sum)


def increment(x, y, t=0):
    """
        Increment 2 x and y number with third paramter t
    """
    return x + t, y + t

output = increment(1,2, 10)
print(output)



