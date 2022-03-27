from src.figure import Figure


class Square(Figure):
    def __init__(self, name, a):
        super().__init__(name, 1)
        if a > 0:
            self.a = a
        else:
            raise ValueError("Square doesn't exist")

    def area(self):
        return self.a ** 2

    def perimeter_square(self):
        return self.a * 4

    def add_area(self, figure):
        return self.area() + figure.area()
