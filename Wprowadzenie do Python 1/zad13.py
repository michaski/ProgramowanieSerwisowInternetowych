# Stwórz program wypisujący dane z listy, która zawiera kilka słowników (dane wypisz w postaci jednego string'a
# odpowiednio go formatując)

lista = [
    dict({"python": "https://www.python.org/", "django": "https://www.djangoproject.com/", "numpy": "https://numpy.org/"}),
    dict({"mysql": "https://www.mysql.com/", "posteSQL": "https://www.postgresql.org/"}),
    dict({"pygtk": "http://www.pygtk.org/", "tkinter": "https://wiki.python.org/moin/TkInter", "wxpython": "https://www.wxpython.org/"})
]

napisWyjsciowy = "Linki:\n"
for slownik in lista:
    for klucz in slownik.keys():
        napisWyjsciowy += "{:>10}: {}".format(klucz, slownik[klucz]) + "\n"

print(napisWyjsciowy)
