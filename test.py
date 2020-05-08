import unittest
import calc
from decimal import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual = calc.execCalc(1133.32, 17539, 27.00,
                               7737, 5330,
                               0.01, 1, 1,
                               0.1, 500, 500)
        self.assertEqual(calc.roundd(24.8), actual[0])
        self.assertEqual(actual[1], 5260)
        self.assertEqual(actual[2], 7602)

#this tests the calc method only, use above for full function
    def test_calc(self):
        actual = calc.runCalc(25, 5260, 7602, 16504, 25.3)
        self.assertEqual(actual, round(Decimal(1174.64), 2))


if __name__ == '__main__':
    unittest.main()
