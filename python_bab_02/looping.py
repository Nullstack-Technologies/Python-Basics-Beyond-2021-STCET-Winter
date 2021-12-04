"""
    Looping Logic in Python
"""


# a = 1
# WHILE LOOP
# 1 > 2
# 2 > 3
# 3 > 4
# 4 > 5
# 5 > 6
# 6 <EXITED>
while a < 6:
    print(a)
    a = a + 1

print("/...../")

a = 1
while a < 6:
    a = a + 1
    print(a)


while(True):
    print("...")


# NESTED  LOOPS
i = 0
j = 0
while i < 3:
    i = i + 1
    while j < 3:
        print(i, j)
        j = j + 1


# break statement
# It breaks out of the loop
i = 1
while i <= 10:
    i += 1  # Shorthand assignment operation i = i + 1
    if i == 5:
        break
    print(i)


print("\t--------")

# continue
# jumps you to the last statement of the loop
i = 1
while i <= 10:
    i += 1  # Shorthand assignment operation i = i + 1
    if i == 5:
        continue
    print(i)




# FOR 
a = [1, 2, 3]
for x in a:
    print(x)

# a = [1, 2, 3]
for x in a:
    for y in a:
        print(x,y)

