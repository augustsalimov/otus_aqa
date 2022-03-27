from src.triangle import Triangle
from src.square import Square

name = 'Triangle'
a = 3
b = 4
c = 5


def test_create_class():
    triangle = Triangle(name, a, b, c)
    assert triangle.sides() == 3
    assert isinstance(triangle, Triangle)


def test_area():
    triangle = Triangle(name, a, b, c)
    assert triangle.area() == 6


def test_perimeter():
    triangle = Triangle(name, a, b, c)
    assert triangle.perimeter_triangle() == 12


def test_add_area():
    square = Square(name, a)
    square.area()
    triangle = Triangle(name, a, b, c)
    triangle.area()
    assert (triangle.add_area(square)) == square.area() + triangle.area()
