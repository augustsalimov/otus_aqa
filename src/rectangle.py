from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, 2)
        if a and b > 0:
            self.a = a
            self.b = b
        else:
            raise ValueError("Rectangle doesn't exist")

    def area(self):
        return self.a * self.b

    def perimeter_rectangle(self):
        return (self.a + self.b) * 2

    def add_area(self, figure):
        return self.area() + figure.area()
