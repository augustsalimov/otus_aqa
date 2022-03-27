from src.figure import Figure


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        super().__init__(name, 3)
        if a + b > c and b + c > a and a + c > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Triangle doesn't exist")
        self._area = 0

    def area(self):
        half_p = (self.a + self.b + self.c) / 2
        return (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5

    def perimeter_triangle(self):
        return self.a + self.b + self.c

    def add_area(self, figure):
        return self.area() + figure.area()
