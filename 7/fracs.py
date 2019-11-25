from fractions import gcd

class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Division by zero. y value cannot be 0")
        self.x = x
        self.y = y

    def __str__(self): 
        if self.y == 1: 
            return str(self.x)
        return "{0}/{1}".format(self.x, self.y)

    def __repr__(self): 
        return "Frac({0}, {y})".format(self.x, self.y)
    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other): 
        s = self.shorten()
        o = other.shorten()
        return s.x == o.x and s.y == o.y

    def __ne__(self, other): 
        return not self == other

    def __lt__(self, other): 
        s, o = self.to_common_denomitor(other)
        return s.x < o.x

    def __le__(self, other): 
        s, o = self.to_common_denomitor(other)
        return s.x <= o.x

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):
        if isinstance(other, int):
            s = self
            o = Frac(other, 1)
        else:
            s, o = self.to_common_denomitor(other)
        return Frac(s.x + o.x, s.y).shorten()

    __radd__ = __add__  

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Frac(self.x * other, self.y).shorten()
        return Frac(self.x * other.x, self.y * other.y).shorten()

    __rmul__ = __mul__ 

    def __truediv__(self, other):
        if isinstance(other, int):
            o = Frac(other, 1)
        o = ~other
        return self * o

    def __rtruediv__(self, other):
        o = self.__invert__()
        return other / o

    def __pos__(self): 
        return self

    def __neg__(self): 
        return self * (-1)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self): 
        return float(self.x / self.y)

    def shorten(self):
        g = gcd(self.x, self.y)
        return Frac(self.x // g, self.y // g)

    def to_common_denomitor(self, other):
        frac1x = self.x
        frac1y = self.y
        frac2x = other.x
        frac2y = other.y
        tmp = frac1y
        frac1x *= frac2y
        frac1y *= frac2y
        frac2x *= tmp
        frac2y *= tmp
        return (Frac(frac1x, frac1y), Frac(frac2x, frac2y))



import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_sub_frac(self): 
        self.assertEqual(Frac(5, 6) - Frac(1, 3), Frac(1, 2))

    def test_mul_frac(self): 
        self.assertEqual(Frac(3, 4) * Frac(1, 3), Frac(1, 4))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 4) / Frac(1, 3), Frac(3, 4))

    def test_eq(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))

    def test_lt(self):
        self.assertTrue(Frac(1, 3) < Frac(2, 4))

    def test_le(self):
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))

    def test_neg(self):
        self.assertTrue(-Frac(1, 2) == Frac(-1, 2))

    def test_invert(self):
        self.assertTrue(~Frac(1, 2) == Frac(2, 1))

    def test_frac2float(self): 
        self.assertTrue(float(Frac(1, 4)) == 0.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy