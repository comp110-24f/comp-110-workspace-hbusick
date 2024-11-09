"""Class 22 Quiz 3 Practice"""

import math


class Circle:
    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        return math.pi * (self.radius**2)


circ: Circle = Circle(r=2)
print(circ.area())


class Rectangle:
    l: float
    w: float

    def __init__(self, l: float, w: float):
        self.length = l
        self.width = w

    def area(self) -> float:
        return self.length * self.width


rect: Rectangle = Rectangle(4, 5.5)
print(rect.area())
