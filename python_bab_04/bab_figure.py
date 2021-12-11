"""
    Inheritance in Classes
"""

class Figure:

    def __init__(self):
        print("Figure Object Initialized")

    def __str__(self):
        return "<Figure Object>"
    
    def area(self):
        print("Area not Implemented")

    def perimeter(self):
        print("Perimeter not Implemented")

# Sub class of Figure
# it has access to all what Figure does
# and it adds its own implementations
class Square(Figure):

    def __init__(self, x):
        self.x = x
        print("Square Object Initialized")
        super().__init__()

    def __str__(self):
        return f"<Square Object with side {self.x}>"


class Rectangle(Figure):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def __str__(self):
        return f"<Rectangle Object with sides {self.length}, {self.breadth}>"
    

# class Triangle:
#     pass







# figure = Figure()
# square = Square()

# print(figure.shape_descriptor())
# print(square.shape_descriptor())


square = Square(5)
# rectangle = Rectangle(10, 5)

# square.area()
# rectangle.perimeter()


    