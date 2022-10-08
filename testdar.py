import unittest
from decimalRoman import Main

class TestRomanToNumber(unittest.TestCase):

    def test_1(self):
        roman = Main.intToRoman(1)
        self.assertEqual(roman, "I")

    def test_2(self):
        roman = Main.intToRoman(2)
        self.assertEqual(roman, "II")

    def test_3(self):
        roman = Main.intToRoman(3)
        self.assertEqual(roman, "III")

    def test_4(self):
        roman = Main.intToRoman(4)
        self.assertEqual(roman, "IV")

    def test_5(self):
        roman = Main.intToRoman(5)
        self.assertEqual(roman, "V")

    def test_6(self):
        roman = Main.intToRoman(6)
        self.assertEqual(roman, "VI")

    def test_7(self):
        roman = Main.intToRoman(7)
        self.assertEqual(roman, "VII")

    def test_10(self):
        roman = Main.intToRoman(10)
        self.assertEqual(roman, "X")

if __name__=='__main__':
    unittest.main()