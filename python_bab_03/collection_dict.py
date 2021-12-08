"""
    Demonstrate a Dictionary in Python
"""

# Ordered
# mutated (Changed)
# Duplicates


# key- value pairs

person = {
    "name": "Nauman Arif",
    "company": "NullStack Technologies",
    "expert_level": 0.001,
    "designation": "Developer"
}

print(person)

# get values
print(person["name"])

# add values 
person["age"] = 100

# update values
person["name"] = "John Doe"

print(person)


# methods
person.pop('expert_level')
print(person)

print(person.keys())
print(person.values())


a = {
    0: 1,
    1: 2,
    2: 3
}
print(a[0])


fruits = {
    '🍇': 'grapes', 
    '🍉': 'watermelon', 
    '🍎': 'apple',
}
print(fruits['🍇'])
print(fruits['🍉'])




person = {
    "name": "Nauman Arif",
    "company": "NullStack Technologies",
    "expert_level": 0.001,
    "designation": "Developer",
    "marks": [
        ({"maths": 90}, {"hindi": 100}, {"programming": 0}),
        ({"maths": 90}, {"hindi": 100}, {"programming": 0})
    ]
}