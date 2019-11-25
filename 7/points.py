import unittest

from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    """Konstruktor"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    """zwraca string "(x, y)"""

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    """zwraca string "Point(x, y)"""

    def __repr__(self):
        return "Point({0},{1})".format(self.x, self.y)

    """obsługa point1 == point2"""

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    """obsługa point1 != point2"""

    def __ne__(self, other):
        return not self == other

    """dodaje punkty jako wektory 2D"""

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    """odejmuje punkty jako wektory 2D"""

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    """iloczyn skalarny"""

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    """iloczyn wektorowy"""

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    """dlugosc wektora"""

    def length(self):
        return sqrt(self * self)


class TestPoint(unittest.TestCase):
    
    def test_print(self):
        assert(str(Point(1,2)) == "(1,2)")
        assert(repr(Point(1,2)) == "Point(1,2)")

    def test_eq(self):
        assert(Point(1,2) == Point(1,2))
        assert(Point(1,2) != Point(2,2))

    def test_add(self):
        self.assertEquals(Point(1, 2) + Point(2, 1), Point(3, 3))

    def test_sub(self):
        self.assertEquals(Point(1, 2) - Point(2, 1), Point(-1, 1))

    def test_mul(self):
        self.assertEquals(Point(1, 2) * Point(2, 1), 4)

    def test_cross(self):
        self.assertEquals(Point(1, 2).cross(Point(2, 1)), -3)

    def test_lenght(self):
        self.assertEquals(Point(3, 4).length(), 5)

if __name__ == "__main__":
    unittest.main()
