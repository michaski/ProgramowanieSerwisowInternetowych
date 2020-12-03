from rest_framework import serializers
from .models import *


class UzytkownikSerializer(serializers.Serializer):
    imie = serializers.CharField(max_length=45, null=False)
    nazwisko = serializers.CharField(max_length=45, null=False)
    nick = models.CharField(max_length=256, null=False)
    email = serializers.EmailField(max_length=45, null=False)
    haslo = serializers.CharField(max_length=45, null=False)


class InstruktorSerializer(serializers.Serializer):
    imie = serializers.CharField(max_length=45, null=False)
    nazwisko = serializers.CharField(max_length=45, null=False)
    biografia = models.CharField(max_length=256, null=False)
    email = serializers.EmailField(max_length=45, null=False)
    haslo = serializers.CharField(max_length=45, null=False)


class KursSerializer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=45, null=False)
    opis = serializers.CharField(max_length=45, null=False)
    cena = serializers.DecimalField(null=False, max_digits=5, decimal_places=2)
    idInstruktora = serializers.PrimaryKeyRelatedField(many=False)

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


class ZasobSerializer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=45, null=False)
    url = serializers.URLField(max_length=45, null=False)
    idLekcji = serializers.PrimaryKeyRelatedField()


class PlatnoscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosc
        fields = ['idUzytkownika', 'idKursu']
