import unittest
from main import *

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


class TestNumberToRoman(unittest.TestCase):

    def test_1(self):
        roman = DecimalToRoman.intToRoman(1)
        self.assertEqual(roman, "I")

    def test_2(self):
        roman = DecimalToRoman.intToRoman(2)
        self.assertEqual(roman, "II")

    def test_3(self):
        roman = DecimalToRoman.intToRoman(3)
        self.assertEqual(roman, "III")

    def test_4(self):
        roman = DecimalToRoman.intToRoman(4)
        self.assertEqual(roman, "IV")

    def test_5(self):
        roman = DecimalToRoman.intToRoman(5)
        self.assertEqual(roman, "V")

    def test_6(self):
        roman = DecimalToRoman.intToRoman(6)
        self.assertEqual(roman, "VI")

    def test_7(self):
        roman = DecimalToRoman.intToRoman(7)
        self.assertEqual(roman, "VII")

    def test_10(self):
        roman = DecimalToRoman.intToRoman(10)
        self.assertEqual(roman, "X")


if __name__=='__main__':
    unittest.main()


