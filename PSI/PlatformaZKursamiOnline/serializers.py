from rest_framework import serializers
from .models import *


class UzytkownikSerializer(serializers.HyperlinkedModelSerializer):
    kupione_kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)
    # kupione_kursy = serializers.SlugRelatedField(queryset=Platnosc.objects.all(), many=True, slug_field='idKursu')

    class Meta:
        model = Uzytkownik
        fields = ['id', 'url', 'imie', 'nazwisko', 'nick', 'email', 'haslo', 'kupione_kursy']


class InstruktorSerializer(serializers.HyperlinkedModelSerializer):
    # kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)

    kursy = serializers.SlugRelatedField(queryset=Kurs.objects.all(), many=True, slug_field='nazwa')

    class Meta:
        model = Instruktor
        fields = ['id', 'url', 'imie', 'nazwisko', 'biografia', 'email', 'haslo', 'kursy']


class KursSerializer(serializers.HyperlinkedModelSerializer):
    # nazwa = serializers.CharField(max_length=45)
    # opis = serializers.CharField(max_length=256)
    # cena = serializers.DecimalField(max_digits=5, decimal_places=2)
    # idInstruktora = serializers.PrimaryKeyRelatedField(many=False)

    # lekcje = serializers.HyperlinkedRelatedField(view_name='lekcja-detail', read_only=True, many=True)

    idInstruktora = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), many=False, slug_field='imie')

    lekcje = serializers.SlugRelatedField(queryset=Lekcja.objects.all(), many=True, slug_field='nazwa')

    class Meta:
        model = Kurs
        fields = ['id', 'url', 'nazwa', 'opis', 'cena', 'idInstruktora', 'lekcje']

    def validate_cena(self, value):
        try:
            cena_flt = float(value)
        except:
            raise serializers.ValidationError('Błędna wartość pola cena - wartość nie jest liczbą')

        if value > 0:
            return value
        else:
            raise serializers.ValidationError('Cena nie może być ujemna')

        # if not isinstance(value, int):
        #     raise serializers.ValidationError('Błędna wartość pola cena')
        # if value > 0:
        #     return value
        # else:
        #     raise serializers.ValidationError('Cena nie może być ujemna')


class LekcjaSerializer(serializers.HyperlinkedModelSerializer):
    # zasoby = serializers.HyperlinkedRelatedField(view_name='zasob-detail', read_only=True, many=True)
    zasoby = serializers.SlugRelatedField(queryset=Zasob.objects.all(), many=True, slug_field='nazwa')
    idKursu = serializers.SlugRelatedField(queryset=Kurs.objects.all(), many=False, slug_field='nazwa')
    idInstruktora = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), many=False, slug_field='imie')

    class Meta:
        model = Lekcja
        fields = ['id', 'url', 'nazwa', 'opis', 'idKursu', 'idInstruktora', 'zasoby']


class ZasobSerializer(serializers.ModelSerializer):
    idLekcji = serializers.SlugRelatedField(queryset=Lekcja.objects.all(), many=False, slug_field='nazwa')

    class Meta:
        model = Zasob
        fields = ['id', 'url', 'nazwa', 'url', 'idLekcji']


class PlatnoscSerializer(serializers.ModelSerializer):
    idKursu = serializers.SlugRelatedField(queryset=Kurs.objects.all(), many=False, slug_field='nazwa')
    idUzytkownika = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), many=False, slug_field='imie')

    class Meta:
        model = Platnosc
        fields = ['id', 'idUzytkownika', 'idKursu']
