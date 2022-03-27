from src.rectangle import Rectangle
from src.circle import Circle

name = 'Circle'
a = 3
b = 4


def test_create_class():
    circle = Circle(name, a)
    assert circle.sides() == 1
    assert isinstance(circle, Circle)


def test_area():
    circle = Circle(name, a)
    assert circle.area() == 28.274333882308138


def test_perimeter():
    circle = Circle(name, a)
    assert circle.perimeter_circle() == 18.84955592153876


def test_add_area():
    circle = Circle(name, a)
    circle.area()
    rectangle = Rectangle(name, a, b)
    rectangle.area()
    assert (circle.add_area(rectangle)) == rectangle.area() + circle.area()
