"""
    Demonstrate a List in Python
"""


# Order -> Ordered
# Duplication -> Allows Duplicate values
# Change the values (Mutability) -> Allows for values to be changed

a = [1, 2, 3]
print(a)
print(a[0])

#🌶️
# ---------6   -5     -4   -3    -2     -1
# -------- 0     1      2    3     4      5
fruits = ['🍇', '🍉', '🍎', '🍒', '🥝', '🍇']

# positive indexes
print(fruits[1])
print(fruits[1:4])
print(fruits[2:])

# negative indexes
print(fruits[-1])
print(fruits[-3:-1])
print(fruits[-5:-2])

# mutation
print(fruits)
fruits[5] = '🌶️'
print(fruits)



# inbuilt methods
a.append('4')
print(a)
# insert(index, value)
a.insert(1, True)

a.extend([5, 6, 7])

# removals
# index
a.pop(1)
# value
a.remove(1)

a.reverse()
a.clear()
a.sort()

print(a)


# index
print(fruits.index('🍉'))

