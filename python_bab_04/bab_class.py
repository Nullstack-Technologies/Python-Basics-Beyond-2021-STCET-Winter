"""
    Implementation of Classes
"""

import math

# EUCILDIAN POINTS
# (x, y)
# class Point:
#     pass

# NAMING ?
# PEP 8
# class PiedPiper:
#     pass




# instance of a class
# Object of a class
# point = Point()
# point_1 = Point()


# (3, 5)
# point.x = 3
# point.y = 5

#print(point.x, point.y)

class Point:
    """
        A Pythonic representation of the Euclidian Point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Point ({self.x}, {self.y})>"

    def __add__(self, obj):
        return self.x + obj.x, self.y + obj.y 

    def __sub__(self, obj):
        return self.x - obj.x, self.y - obj.y 

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y
    
    def distance(self, obj):
        """
            Computes the distance between two Euclidian Points:
            P1(x1, y1 ) and P2(x2, y2) dist(P1, P2) = 
        """
        dist = math.sqrt((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2)
        dist = round(dist, 2)
        return dist
    
    def display_x_and_y(self):
        print(f"<Point ({self.x}, {self.y})>")



point_1 = Point(3, 5)
# print(point_1.x, point_1.y)

point_2 = Point(5, 10)
# print(point_2.x, point_2.y)

# point_check = Point()

# point_1.display_x_and_y()
# point_2.display_x_and_y()

print(point_1 + point_2)
print(point_2 + point_1)

print(point_1 - point_2)
print(point_2 - point_1)

print(point_2 == point_1)


print(point_1.distance(point_2))








