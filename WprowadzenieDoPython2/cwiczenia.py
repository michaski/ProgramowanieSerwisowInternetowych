import math
from WprowadzenieDoPython2 import file_manager


# zad1
def zlaczenie_list(a_list, b_list):
    wynik = []
    for i in range(0, len(a_list)):
        if i % 2 == 1:
            wynik.append(a_list[i])
        else:
            wynik.append(b_list[i])
    return wynik


print(zlaczenie_list(['a', 'b', 'c', 'd'], ['w', 'x', 'y', 'z']))

# zad2


def info_o_parametrze(data_text):
    return {
        "length": len(data_text),
        "letters": [data_text[i] for i in range(0, len(data_text)) if data_text[i].isalpha()],
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }


print(info_o_parametrze("Lorem Ipsum"))

# zad3


def usun_litery(text, letter):
    return text.replace(letter, "")


print(usun_litery("Lorem Ipsum", 'm'))

# zad4


def przelicz_temperature(temp_w_c, temperature_type):
    temperature_type = temperature_type.lower()
    if temperature_type == 'k':
        return temp_w_c + 273.15
    elif temperature_type == 'f':
        return 32 + (1.8 * temp_w_c)
    elif temperature_type == 'r':
        return 1.8 * (temp_w_c + 273.15)
    else:
        return "Zły rodzaj temperatury"


print(przelicz_temperature(22, 'K'))
print(przelicz_temperature(22, 'f'))
print(przelicz_temperature(22, 'R'))
print(przelicz_temperature(22, 'x'))

# zad 5


class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def difference(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return None
        return num1 / num2


class ScienceCalculator(Calculator):
    def __init__(self):
        pass

    def pow(self, num1, num2):
        return math.pow(num1, num2)

    def modulo(self, num1, num2):
        return num1 % num2

    def sqrt(self, num):
        return math.sqrt(num)

# zad 6


def wypisz_od_tylu(napis):
    print(napis[::-1])


wypisz_od_tylu("koteł")

fm = file_manager.FileManager("plik.txt")
fm.update_file("Hello, World!")
print(fm.read_file())


