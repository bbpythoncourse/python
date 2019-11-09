from fractions import gcd

def shorten(frac):
    g = gcd(frac[0], frac[1])
    return [frac[0] // g, frac[1] // g]

def add_frac(frac1, frac2):             # frac1 + frac2
    tmp = frac1[1]
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[1]
    frac2[0] *= tmp
    frac2[1] *= tmp

    assert(frac2[1] == frac2[1])

    result = [frac1[0] + frac2[0], frac2[1]]
    return shorten(result)


def sub_frac(frac1, frac2):             # frac1 - frac2
    tmp = frac1[1]
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[1]
    frac2[0] *= tmp
    frac2[1] *= tmp

    assert(frac2[1] == frac2[1])

    result = [frac1[0] - frac2[0], frac2[1]]
    return shorten(result)


def mul_frac(frac1, frac2):             # frac1 * frac2
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return shorten(result)


def div_frac(frac1, frac2):             # frac1 / frac2
    inversed = [frac2[1], frac2[0]]
    return mul_frac(frac1, inversed)


def is_positive(frac):                  # bool, czy dodatni
    return (frac[0] > 0 and frac[1]) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):                      # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    tmp = frac1[1]
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[1]
    frac2[0] *= tmp
    frac2[1] *= tmp

    assert(frac2[1] == frac2[1])

    if frac1[0] > frac2[1]: return 1
    if frac1[0] < frac2[1]: return -1
    return 0


def frac2float(frac):                   # konwersja do float
    return frac[0] / frac[1]



import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([5, 6], [1, 3]), [1, 2])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([3, 4], [1, 3]), [1, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 4], [1, 3]), [3, 4])

    def test_is_positive(self):
        self.assertTrue(is_positive([-3, -4]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 3]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 4], [1, 3]), -1)

    def test_frac2float(self): 
        self.assertEqual(frac2float([1, 4]), 0.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy