"""
    Conditional Logics in Python
"""

# If
a = float(input("Please give an a: "))
b = float(input("Please give an b: "))

if a == 3:
    print("You gave 3")
    print("If scope")


# a is > 10 and a is even
if a > 10 and a % 2 == 0:
    print("Passed")


# else
if a > 10 and a % 2 == 0:
    print("Passed")
else:
    print("Not Passed")


# b > a ok, else if a == b print something else, and otherwise its ok
# BAD CODE ? KNow why?
if b > a:
    print("b is greater than a")
elif a == b:
    print("b is equal to a")
elif b < a :
    print("b is less than a")
else:
    print("Nevermind!")


# IF, ELSE, ELIF Ladder
if b > a:
    print("b is greater than a")
elif a == b:
    print("b is equal to a")
else:
    print("b is less than a")


# NESTED IF _ ELSE
# is a > b?
if a >= b:
    # is a equal to b ?
    if a == b:
        print("a is equal to b")
    # Now a has to be greater than b?
    else:
        print("a is greater than b")
# Now a has to be less than b?
else:
    print("a is less than b")



# SHORTHAND
# expressionIF if <condition > else expressionELSE
print("a is greater than b") if a > b else print("a is lesser than b")
print("a is greater than b") if (a > b) else (print("a is equal to b") if a == b else print("a is lesser than b"))