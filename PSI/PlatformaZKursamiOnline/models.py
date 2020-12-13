from django.db import models

# Create your models here.


class Uzytkownik(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    nick = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    haslo = models.CharField(max_length=45, null=False)


class Instruktor(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    biografia = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=45, null=False)
    haslo = models.CharField(max_length=45, null=False)


class Kurs(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    cena = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1)


class Lekcja(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1)


class Zasob(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    url = models.CharField(max_length=256, null=False)
    idLekcji = models.ForeignKey(Lekcja, on_delete=models.CASCADE)


class Platnosc(models.Model):
    idUzytkownika = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE)
