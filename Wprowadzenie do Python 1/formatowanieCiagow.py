print("=Wyrównanie tekstu=")
print("{:20}".format("Do lewej"))
print("{:>20}".format("Do prawej"))
print("{:^20}".format("Do środka"))

print("=Obcinanie długich napisów=")
napis = "Dłuuugi tekst"
print(f"Oryginalnie: {napis}")
print("Po obcięciu (długość 10 znaków): {:.10}".format(napis))

print("=Ilość pozycji liczby=")
jakasLiczba = 123
print(f"Liczba:\n{jakasLiczba}")
print("Ta sama liczba zapisana na 5 miejscach:\n{:5d}".format(jakasLiczba))
print("Ta sama liczba zapisana na 5 miejscach z zerami wiodącymi:\n{:05d}".format(jakasLiczba))
jakasLiczba /= 10
print(f"Działa też z liczbami zmiennoprzecinkowymi:\n{jakasLiczba}")
print("Ta sama liczba zapisana na 5 miejscach:\n{:5.1f}".format(jakasLiczba))
print("Ta sama liczba zapisana na 5 miejscach z zerami wiodącymi:\n{:05.1f}".format(jakasLiczba))

print("=Liczba ze znakiem=")
print("{:+d}".format(15))
print("{: d}".format(15))
print("{: d}".format(-15))

print("=Formatowanie parametryzowane=")
print("Wyśrodkowany napis o szerokości 30")
print("{:{wyrownanie}{szerokosc}}".format("Python", wyrownanie="^", szerokosc="30"))
print("Dokładność wypisywania")
print("{:.{prec}} = {:.{prec2}f}".format("długość", 12.158, prec=2, prec2=1))
