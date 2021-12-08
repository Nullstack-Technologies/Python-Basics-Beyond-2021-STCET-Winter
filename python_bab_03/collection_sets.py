"""
    Demonstrate a Sets in Python
"""


# Order -> Unordered
# Unindexed
# Duplication -> Not Duplicates
# Change the values (Mutability) -> Allows

a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2}

# print(a)
# a.add(6)
# print(a)

# a.remove(6)
# print(a)


print(a.union(b))
print(a.intersection(b))
print(c.issubset(a))
print(c.issubset(b))

print(a.issuperset(c))


print(a.isdisjoint(c))
print(b.isdisjoint(c))



# a.clear()
# print(a)







#🌶️
# ---------6   -5     -4   -3    -2     -1
# -------- 0     1      2    3     4      5
# fruits = ['🍇', '🍉', '🍎', '🍒', '🥝', '🍇']