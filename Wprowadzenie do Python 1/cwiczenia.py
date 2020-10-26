tekstCzymJestLoremIpsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle " \
                          "poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do " \
                          "wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle " \
                          "elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX " \
                          "w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z " \
                          "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków " \
                          "na komputerach osobistych, jak Aldus PageMaker "

imie = "Michał"
nazwisko = "Krzyżanowski"

print(f"W tekście jest {tekstCzymJestLoremIpsum.count(imie[1])} liter {imie[1]} oraz "
      f"{tekstCzymJestLoremIpsum.count(nazwisko[2])} liter {nazwisko[2]}.")

# print(dir(imie))
# help(imie.isprintable())

print(f"{nazwisko[::-1].capitalize()} {imie[::-1].capitalize()}")

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista1[5:]
lista1 = lista1[:5]
print(lista1)
print(lista2)

listaStudentow = [
    (150800, "Michał Krzyżanowski"),
    (123741, "Jan Kowalski"),
    (463819, "Tomasz Nowak"),
    (574820, "Szymon Kowalczyk"),
    (123418, "Stanisław Wiśniewski")
]

slownik = dict(listaStudentow)
print(slownik)
slownik[483012] = (21, "483012@student.uczelnia.edu.pl", 1999, "Dębowa 1")
slownik[643782] = (23, "643782@student.uczelnia.edu.pl", 1997, "Akacjowa 1")
print(slownik)

listaNrTelefonow = [859463741, 657483926, 563728195, 859463741, 436281932, 657483926]
print(listaNrTelefonow)
print(set(listaNrTelefonow))

for i in range(1, 11):
    print(i, end=" ")

print()

for i in range(100, 19, -5):
    print(i, end=" ")

print()
