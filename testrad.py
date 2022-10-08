import unittest
from mainrad import Main


class TestRomanToNumber(unittest.TestCase):

    def test_1(self):
        decimal_number = Main.roman_to_int("I")
        self.assertEqual(decimal_number, 1)

    def test_2(self):
        decimal_number = Main.roman_to_int('II')
        self.assertEqual(decimal_number, 2)

    def test_3(self):
        decimal_number = Main.roman_to_int('III')
        self.assertEqual(decimal_number, 3)

    def test_4(self):
        decimal_number = Main.roman_to_int('IV')
        self.assertEqual(decimal_number, 4)

    def test_5(self):
        decimal_number = Main.roman_to_int('V')
        self.assertEqual(decimal_number, 5)

    def test_9(self):
        decimal_number = Main.roman_to_int('IX')
        self.assertEqual(decimal_number, 9)

    def test_10(self):
        decimal_number = Main.roman_to_int('X')
        self.assertEqual(decimal_number, 10)


if __name__=='__main__':
    unittest.main()


