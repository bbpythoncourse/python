import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("x1 needs to be lesser than x2 and y1 needs to be lesser than y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):      
        return "[({0}, {1}), ({2}, {3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):     
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):    
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):      
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

    def intersection(self, other):
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):
        r1 = Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x - self.pt1.x) / 2, (self.pt2.y - self.pt1.y) / 2)
        r2 = Rectangle((self.pt2.x - self.pt1.x) / 2, self.pt1.y, self.pt2.x, (self.pt2.y - self.pt1.y) / 2)
        r3 = Rectangle(self.pt1.x, (self.pt2.y - self.pt1.y) / 2, (self.pt2.x - self.pt1.x) / 2, self.pt2.y)
        r4 = Rectangle((self.pt2.x - self.pt1.x) / 2, (self.pt2.y - self.pt1.y) / 2, self.pt2.x, self.pt2.y)
        return (r1, r2, r3, r4)
# Kod testujący moduł.


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

    def test_intersection(self):
        self.assertTrue(Rectangle(1, 3, 5, 8).intersection(Rectangle(2, 4, 7, 9)) == Rectangle(2, 4, 5, 8))

    def test_cover(self):
        self.assertTrue(Rectangle(1, 3, 5, 8).cover(Rectangle(2, 4, 7, 9)) == Rectangle(1, 3, 7, 9))

    def test_invalid_data(self):
        self.assertRaises(ValueError, Rectangle, 5, 1, 3, 1)


if __name__ == "__main__":
    unittest.main()
