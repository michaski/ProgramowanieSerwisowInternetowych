from rest_framework import serializers
from .models import *


class UzytkownikSerializer(serializers.HyperlinkedModelSerializer):
    kupione_kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)

    class Meta:
        model = Uzytkownik
        fields = ['id', 'url', 'imie', 'nazwisko', 'nick', 'email', 'haslo', 'kupione_kursy']


class InstruktorSerializer(serializers.HyperlinkedModelSerializer):
    kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)

    class Meta:
        model = Instruktor
        fields = ['id', 'url', 'imie', 'nazwisko', 'biografia', 'email', 'haslo', 'kursy']


class KursSerializer(serializers.HyperlinkedModelSerializer):
    # nazwa = serializers.CharField(max_length=45)
    # opis = serializers.CharField(max_length=256)
    # cena = serializers.DecimalField(max_digits=5, decimal_places=2)
    # idInstruktora = serializers.PrimaryKeyRelatedField(many=False)

    lekcje = serializers.HyperlinkedRelatedField(view_name='lekcja-detail', read_only=True, many=True)

    # idInstruktora = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), many=False, slug_field='imie')

    # lekcje = serializers.SlugRelatedField(queryset=Lekcja.objects.all(), many=True, slug_field='nazwa')

    class Meta:
        model = Kurs
        fields = ['id', 'url', 'nazwa', 'opis', 'cena', 'idInstruktora', 'lekcje']

    def validate_cena(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError('Błędna wartość pola cena')
        if value > 0:
            return value
        else:
            raise serializers.ValidationError('Cena nie może być ujemna')


class LekcjaSerializer(serializers.HyperlinkedModelSerializer):
    zasoby = serializers.HyperlinkedRelatedField(view_name='zasob-list', read_only=True, many=True)

    class Meta:
        model = Lekcja
        fields = ['id', 'url', 'nazwa', 'opis', 'idKursu', 'idInstruktora', 'zasoby']


class ZasobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zasob
        fields = ['id', 'url', 'nazwa', 'url', 'idLekcji']


class PlatnoscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosc
        fields = ['id', 'idUzytkownika', 'idKursu']
