#Abel Carrizo
class RomantoDecimal:
    def __init__(self, roman):
        self.values = (('M', 1000),('CM', 900),('D', 500), ('CD', 400),('C', 100),('XC', 90),('L', 50),('XL', 40),
            ('X', 10),('IX', 9),('V', 5),('IV', 4),('I', 1))
        self.result = 0
        self.list = []
        self.roman = roman

    def roman_to_int(self):
        if self.roman.upper().count("X")>3 or self.roman.upper().count("I")>3 or self.roman.upper().count("V")>3 or self.roman.upper().count("L")>3 or self.roman.upper().count("D")>3 or self.roman.upper().count("M")>3:
            print("X")
        else:
            for i in range(len(self.roman.upper())):
                for letter, value in self.values:
                    if self.roman.upper()[i] == letter:
                        self.list.append(value)
            self.list.append(0)

            for i in range(len(self.roman.upper())):
                if self.list[i] >= self.list[i+1]:
                    self.result += self.list[i]
                else:
                    self.result -= self.list[i]
        return self.result