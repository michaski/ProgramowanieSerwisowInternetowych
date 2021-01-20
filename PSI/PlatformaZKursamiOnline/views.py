from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import *
from .serializers import *

# Create your views here.


class KursListView(generics.ListCreateAPIView):
    name = 'lista-kursow'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'informacje_o_kursie'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class LekcjaListView(generics.ListCreateAPIView):
    name = 'lista_lekcji'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer


class LekcjaDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'informacje_o_lekcji'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer


class ZasobListView(generics.ListAPIView):
    name = 'lista_zasobow'
    queryset = Zasob.objects.all()
    serializer_class = ZasobSerializer


class PlatnoscListView(generics.ListCreateAPIView):
    name = 'lista_platnosci'
    queryset = Platnosc.objects.all()
    serializer_class = PlatnoscSerializer


class InstruktorListView(generics.ListCreateAPIView):
    name = 'lista_instuktorow'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer


class InstruktorDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'informacje_o_instruktorze'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer


class UzytkownikListView(generics.ListCreateAPIView):
    name = 'lista_uzytkownikow'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer


class UzytkownikDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'informacje_o_uzytkowniku'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        data = {
            'kursy': reverse(KursListView.name, request=request),
            'instruktorzy': reverse(InstruktorListView.name, request=request),
            'uzytkownicy': reverse(UzytkownikListView.name, request=request),
            'platnosci': reverse(PlatnoscListView.name, request=request),
        }
        return Response(data)
