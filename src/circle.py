import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, name, r):
        super().__init__(name, 1)
        if r > 0:
            self.r = r
        else:
            raise ValueError("Circle doesn't exist")

    def area(self):
        return math.pi * (self.r ** 2)

    def perimeter_circle(self):
        return 2 * math.pi * self.r

    def add_area(self, figure):
        return self.area() + figure.area()
