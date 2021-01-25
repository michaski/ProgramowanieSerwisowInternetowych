from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Uzytkownik(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    nick = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    haslo = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('nazwisko', 'imie')

    def __str__(self):
        return " ".join((self.imie, self.nazwisko))


class Instruktor(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    biografia = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=45, null=False)
    haslo = models.CharField(max_length=45, null=False)

    class Meta:
        ordering = ('nazwisko', 'imie')

    def __str__(self):
        return " ".join((self.imie, self.nazwisko))


class Kurs(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    cena = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1, related_name='kursy')

    class Meta:
        ordering = ('nazwa', )

    def __str__(self):
        return self.nazwa


class Lekcja(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='lekcje')
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1)

    class Meta:
        ordering = ('idKursu', )

    def __str__(self):
        return "->".join((self.idKursu.__str__(), self.nazwa))


class Zasob(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    url = models.CharField(max_length=256, null=False)
    idLekcji = models.ForeignKey(Lekcja, on_delete=models.CASCADE, related_name='zasoby')

    class Meta:
        ordering = ('idLekcji', )

    def __str__(self):
        return self.nazwa


class Platnosc(models.Model):
    idUzytkownika = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, related_name='kupione_kursy')
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE)
