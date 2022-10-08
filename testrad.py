import unittest
from romantoDecimal import RomantoDecimal

class TestRomanToNumber(unittest.TestCase):
    def testI(self):
        roman = RomantoDecimal('I')
        self.assertEqual(roman.roman_to_int(), 1)

    def testII(self):
        roman = RomantoDecimal('II')
        self.assertEqual(roman.roman_to_int(), 2)

    def testIV(self):
        roman = RomantoDecimal('IV')
        self.assertEqual(roman.roman_to_int(), 4)

    def testX(self):
        roman = RomantoDecimal('X')
        self.assertEqual(roman.roman_to_int(), 10)

    def testL(self):
        roman = RomantoDecimal('L')
        self.assertEqual(roman.roman_to_int(), 50)

if __name__=='__main__':
    unittest.main()


