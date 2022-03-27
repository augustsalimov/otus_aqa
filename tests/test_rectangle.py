from src.circle import Circle
from src.rectangle import Rectangle

name = 'Rectangle'
a = 3
b = 4


def test_create_class():
    rectangle = Rectangle(name, a, b)
    assert rectangle.sides() == 2
    assert isinstance(rectangle, Rectangle)


def test_area():
    rectangle = Rectangle(name, a, b)
    assert rectangle.area() == 12


def test_perimeter():
    rectangle = Rectangle(name, a, b)
    assert rectangle.perimeter_rectangle() == 14


def test_add_area():
    rectangle = Rectangle(name, a, b)
    rectangle.area()
    circle = Circle(name, a)
    circle.area()
    assert (rectangle.add_area(circle)) == rectangle.area() + circle.area()
