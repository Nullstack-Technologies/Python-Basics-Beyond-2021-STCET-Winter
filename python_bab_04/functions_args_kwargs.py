"""
    Functions 2.0
"""


# def add(x, y):
#     return x + y


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

# a = input("Give Numbers to add separated by commas:")
# add(a.split(','))
print(add(1, 2, 3, 4, 5))



def name(**kwargs):
    for item in kwargs.keys():
        print(item)
    for item in kwargs.values():
        print(item)

name(first_name="Nauman", last_name="Arif")



# GOD MODE OF PARAMTER PASSING
def add(*args, **kwargs):
    pass
