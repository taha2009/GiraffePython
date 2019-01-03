import unittest
from library.Calc import Calc


class TestStringMethods(unittest.TestCase):
    def test_add(self):
        c = Calc(2, 5)
        self.assertEqual(c.add(), 7)

    def test_multiply(self):
        c = Calc(2, 5)
        self.assertEqual(c.multiply(), 10)


class TestStringMethods2(unittest.TestCase):
    def test_devide(self):
        c = Calc(8, 2)
        self.assertEqual(c.divide(), 4)

    def test_devide_2(self):
        c = Calc(2, 8)
        self.assertEqual(c.divide(), 0.25)


if __name__ == '__main__':
    unittest.main()
