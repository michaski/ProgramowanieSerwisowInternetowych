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
    name = 'kurs-list'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'kurs-detail'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class LekcjaListView(generics.ListCreateAPIView):
    name = 'lekcja-list'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer


class LekcjaDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'lekcja-detail'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer


class ZasobListView(generics.ListCreateAPIView):
    name = 'zasob-list'
    queryset = Zasob.objects.all()
    serializer_class = ZasobSerializer


class ZasobDetailView(generics.RetrieveAPIView):
    name = 'zasob-detail'
    queryset = Zasob.objects.all()
    serializer_class = ZasobSerializer


class PlatnoscListView(generics.ListCreateAPIView):
    name = 'platnosc-list'
    queryset = Platnosc.objects.all()
    serializer_class = PlatnoscSerializer


class InstruktorListView(generics.ListCreateAPIView):
    name = 'instruktor-list'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer


class InstruktorDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'instruktor-detail'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer


class UzytkownikListView(generics.ListCreateAPIView):
    name = 'uzytkownik-list'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer


class UzytkownikDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'uzytkownik-detail'
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
            'lekcje': reverse(LekcjaListView.name, request=request),
            'zasoby': reverse(ZasobListView.name, request=request),
        }
        return Response(data)
