from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UzytkownikSerializer(serializers.HyperlinkedModelSerializer):
    kupione_kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)

    class Meta:
        model = Uzytkownik
        fields = ['id', 'url', 'imie', 'nazwisko', 'nick', 'email', 'slug', 'kupione_kursy']


class InstruktorSerializer(serializers.HyperlinkedModelSerializer):
    # kursy = serializers.HyperlinkedRelatedField(view_name='kurs-detail', read_only=True, many=True)

    kursy = serializers.SlugRelatedField(queryset=Kurs.objects.all(), many=True, slug_field='nazwa')

    class Meta:
        model = Instruktor
        fields = ['id', 'url', 'imie', 'nazwisko', 'biografia', 'email', 'nick', 'slug', 'kursy']


class KursSerializer(serializers.HyperlinkedModelSerializer):

    idInstruktora = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), many=False, slug_field='slug')

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


class LekcjaSerializer(serializers.HyperlinkedModelSerializer):
    # zasoby = serializers.HyperlinkedRelatedField(view_name='zasob-detail', read_only=True, many=True)
    zasoby = serializers.SlugRelatedField(queryset=Zasob.objects.all(), many=True, slug_field='nazwa')
    idKursu = serializers.SlugRelatedField(queryset=Kurs.objects.all(), many=False, slug_field='nazwa')
    idInstruktora = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), many=False, slug_field='slug')

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
    idUzytkownika = serializers.SlugRelatedField(queryset=Uzytkownik.objects.all(), many=False, slug_field='slug')

    class Meta:
        model = Platnosc
        fields = ['id', 'idUzytkownika', 'idKursu']
