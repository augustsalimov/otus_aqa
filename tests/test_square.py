from src.square import Square
from src.triangle import Triangle

name = 'Square'
a = 3
b = 4
c = 5


def test_create_class():
    square = Square(name, a)
    assert square.sides() == 1
    assert isinstance(square, Square)


def test_area():
    square = Square(name, a)
    assert square.area() == 9


def test_perimeter():
    square = Square(name, a)
    assert square.perimeter_square() == 12


def test_add_area():
    square = Square(name, a)
    square.area()
    triangle = Triangle(name, a, b, c)
    triangle.area()
    assert (square.add_area(triangle)) == square.area() + triangle.area()
