from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import *
from .serializers import *
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from django_filters import AllValuesFilter, NumberFilter, FilterSet

# Create your views here.


class CenaFilter(FilterSet):
    cena_od = NumberFilter(field_name='cena', lookup_expr='gte')
    cena_do = NumberFilter(field_name='cena', lookup_expr='lte')
    idInstruktora = AllValuesFilter(field_name='idInstruktora__imie')

    class Meta:
        model = Kurs
        fields = ['cena_od', 'cena_do', 'idInstruktora']


class KursListView(generics.ListCreateAPIView):
    name = 'kurs-list'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    filter_class = CenaFilter
    search_fields = ['nazwa', 'idInstruktora']
    ordering_fields = ['nazwa', 'cena', 'idInstruktora']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(idInstruktora=self.request.user)


class KursDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'kurs-detail'
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class LekcjaListView(generics.ListCreateAPIView):
    name = 'lekcja-list'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer
    filter_fields = ['idKursu']
    search_fields = ['nazwa', 'idKursu']
    ordering_fields = ['idKursu', 'id', 'nazwa']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class LekcjaDetailView(generics.RetrieveUpdateDestroyAPIView):
    name = 'lekcja-detail'
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ZasobListView(generics.ListCreateAPIView):
    name = 'zasob-list'
    queryset = Zasob.objects.all()
    serializer_class = ZasobSerializer
    filter_fields = ['idLekcji']
    search_fields = ['nazwa', 'idLekcji']
    ordering_fields = ['idLekcji', 'id', 'nazwa']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ZasobDetailView(generics.RetrieveAPIView):
    name = 'zasob-detail'
    queryset = Zasob.objects.all()
    serializer_class = ZasobSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class PlatnoscListView(generics.ListCreateAPIView):
    name = 'platnosc-list'
    queryset = Platnosc.objects.all()
    serializer_class = PlatnoscSerializer
    filter_fields = ['idKursu', 'idUzytkownika']
    search_fields = ['idUzytkownika', 'idKursu']
    ordering_fields = ['idKursu', 'idUzytkownika']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class InstruktorListView(generics.ListAPIView):
    name = 'instruktor-list'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer
    filter_fields = []
    search_fields = ['imie', 'nazwisko', 'idKursu']
    ordering_fields = ['nazwisko', 'imie']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class InstruktorDetailView(generics.RetrieveAPIView):
    name = 'instruktor-detail'
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class UzytkownikListView(generics.ListAPIView):
    name = 'uzytkownik-list'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer
    filter_fields = []
    search_fields = ['imie', 'nazwisko']
    ordering_fields = ['nazwisko', 'imie']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class UzytkownikDetailView(generics.RetrieveAPIView):
    name = 'uzytkownik-detail'
    queryset = Uzytkownik.objects.all()
    serializer_class = UzytkownikSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


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
