from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Uzytkownik(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    nick = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    slug = models.SlugField(max_length=90)

    class Meta:
        ordering = ('nazwisko', 'imie', 'slug')

    def __str__(self):
        return self.slug


class Instruktor(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    biografia = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=45, null=False)
    nick = models.CharField(max_length=45, null=False)
    slug = models.SlugField(max_length=90)
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('nazwisko', 'imie', 'slug')

    def __str__(self):
        return self.slug


class Kurs(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    cena = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1, related_name='kursy')

    class Meta:
        ordering = ('nazwa', 'cena', 'idInstruktora')

    def __str__(self):
        return self.nazwa


class Lekcja(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    opis = models.CharField(max_length=256, null=False)
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='lekcje')
    idInstruktora = models.ForeignKey(Instruktor, models.SET_DEFAULT, default=1)

    class Meta:
        ordering = ('idKursu', 'id', 'nazwa')

    def __str__(self):
        return "->".join((self.idKursu.__str__(), self.nazwa))


class Zasob(models.Model):
    nazwa = models.CharField(max_length=45, null=False)
    url = models.CharField(max_length=256, null=False)
    idLekcji = models.ForeignKey(Lekcja, on_delete=models.CASCADE, related_name='zasoby')

    class Meta:
        ordering = ('idLekcji', 'id', 'nazwa')

    def __str__(self):
        return self.nazwa


class Platnosc(models.Model):
    idUzytkownika = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, related_name='kupione_kursy')
    idKursu = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    class Meta:
        ordering = ('idKursu', 'idUzytkownika')
