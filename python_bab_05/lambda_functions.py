"""
    Lambda Functions are one-lined functions
"""


# def add(x, y):
#     return x + y


# def shout(message):
#     return message.upper()

shout = lambda x: x.upper()


add = lambda x, y: x + y


print(shout("Nauman"))
print(add(1, 2))