class Main:
    def roman_to_int(self):
    #Lista
        values = (("M", 1000),("CM", 900),("D", 500), ("CD", 400),("C", 100),("XC", 90),("L", 50),("XL", 40),
            ("X", 10),("IX", 9),("V", 5),("IV", 4),("I", 1))

        result = 0
        lista = []
        romano = input("ROMANO: ")

        if romano.upper().count("X")>3 or romano.upper().count("I")>3 or romano.upper().count("V")>3 or romano.upper().count("L")>3 or romano.upper().count("D")>3 or romano.upper().count("M")>3:
       
            print("[X]")

        else:

            for i in range(len(romano.upper())):
                for letter, value in values:
                    if romano.upper()[i] == letter:
                        lista.append(value)

            lista.append(0)

            for i in range(len(romano.upper())):
                if lista[i] >= lista[i+1]:
                    result = result + lista[i]
                else:
                    result = result - lista[i]

        print("\t-------------",result,"-------------")

if __name__=='__main__':
    a = Main.roman_to_int('I')
    print(a)