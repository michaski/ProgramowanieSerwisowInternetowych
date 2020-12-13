from rest_framework import serializers
from .models import *


class UzytkownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzytkownik
        fields = ['imie', 'nazwisko', 'nick', 'email', 'haslo']


class InstruktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruktor
        fields = ['imie', 'nazwisko', 'biografia', 'email', 'haslo']


class KursSerializer(serializers.ModelSerializer):
    # nazwa = serializers.CharField(max_length=45)
    # opis = serializers.CharField(max_length=256)
    # cena = serializers.DecimalField(max_digits=5, decimal_places=2)
    # idInstruktora = serializers.PrimaryKeyRelatedField(many=False)

    class Meta:
        model = Kurs
        fields = ['nazwa', 'opis', 'cena', 'idInstruktora']

    def validate_cena(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError('Błędna wartość pola cena')
        if value > 0:
            return value
        else:
            raise serializers.ValidationError('Cena nie może być ujemna')


class LekcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lekcja
        fields = ['nazwa', 'opis', 'idKursu', 'idInstruktora']


class ZasobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zasob
        fields = ['nazwa', 'url', 'idLekcji']


class PlatnoscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosc
        fields = ['idUzytkownika', 'idKursu']
