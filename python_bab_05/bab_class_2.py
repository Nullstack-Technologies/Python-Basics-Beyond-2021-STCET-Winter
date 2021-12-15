"""
    Classes in Python - A Brief Introduction
"""

class Person:
    """
        Pythonic Implementation of a Real World Person
    """    

    # MALE = 0
    # FEMALE = 1

    def __init__(self, *args, **kwargs):
        self.first_name = kwargs.get("first_name", args[0])
        self.last_name = kwargs.get("last_name", args[1])
        self.age = kwargs.get("age", args[2])


    def __str__(self):
        return f"Person Class {self.first_name} {self.last_name}"

    def __eq__(self, obj):
        return self.age == obj.age
    
    # DON'T DO THIS
    # use self for instance reference
    def full_name(myself):
        return f"{myself.first_name} {myself.last_name}"

# person = Person("Nauman", "Arif")
# person_1 = Person("John", "Doe")
# print(person.full_name())
# print(person_1.full_name())
# # print(person.first_name)

# print(person.MALE)
# print(person_1.MALE)

# person.MALE = 1

# print(person.MALE)
# print(person_1.MALE)


# INHERITANCE
class Employee(Person):

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        # self.first_name = first_name
        # self.last_name = last_name
        # self.age = age
        # Person.__init__(self, first_name, last_name, age)
        super().__init__(*args, **kwargs)
        self.annual_income = kwargs.get("annual_income", args[3])
    
    def __str__(self):
        # print(super().__str__())
        return f"Employee Class {self.first_name} {self.last_name} {self.annual_income}"


employee = Employee("Nauman", "Arif", 100, 30)
employee_1 = Employee("John", "Dow", 99, 40)

employee_2 = Employee(
    first_name="John", last_name="Dow",
    age=99, annual_income=40,
)


print(employee)
print(employee_1)
print(employee_2)
