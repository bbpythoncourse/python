from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):             # pole powierzchni
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 
    
    def test_print(self):
        assert(str(Rectangle(2, 1, 3, 4)) == "[(2, 1), (3, 4)]")
        assert(repr(Rectangle(2, 1, 3, 4)) == "Rectangle(2, 1, 3, 4)")

    def test_equality(self):
        assert(Rectangle(2, 1, 3, 4) == Rectangle(2, 1, 3, 4))
        assert(Rectangle(2, 1, 3, 4) != Rectangle(2, 2, 3, 4))

    def test_center(self):
        assert(Rectangle(2, 2, 4, 4).center() == Point(3, 3))

    def test_area(self):
        assert(Rectangle(2, 2, 4, 4).area() == 4)

    def test_move(self):
        r = Rectangle(2, 2, 4, 4)
        r.move(4, 3)
        assert(r == Rectangle(6, 5, 8, 7))


if __name__ == "__main__":
    unittest.main()
