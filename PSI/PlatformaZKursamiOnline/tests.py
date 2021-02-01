from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from . import views
from .models import *
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode

# Create your tests here.


# class UzytkownikTests(APITestCase):
#     def post_uzytkownik(self, imie, nazwisko, nick, email, slug):
#         url = reverse(views.UzytkownikListView.name)
#         data = {
#             'imie': imie,
#             'nazwisko': nazwisko,
#             'nick': nick,
#             'email': email,
#             'slug': slug
#         }
#         response = self.client.post(url, data, format='json')
#         return response
#
#     def test_post_and_get_uzytkownik(self):
#         nowe_imie = 'JanTest'
#         nowe_nazwisko = 'Testowalski'
#         nowy_email = 'test@mail.com'
#         nowy_nick = 'testowy'
#         nowy_slug = 'JanTest_Testowalski'
#         response = self.post_uzytkownik(nowe_imie, nowe_nazwisko, nowy_nick, nowy_email,
#                                         nowy_slug)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Uzytkownik.objects.count() == 1
#         assert Uzytkownik.objects.get().nick == nowy_nick
#
#
# class InstruktorTests(APITestCase):
#     def post_instruktor(self, imie, nazwisko, biografia, email, nick, slug):
#         url = reverse(views.InstruktorListView.name)
#         data = {'imie': imie,
#                 'nazwisko': nazwisko,
#                 'biografia': biografia,
#                 'email': email,
#                 'nick': nick,
#                 'slug': slug,
#                 'kursy': []}
#         response = self.client.post(url, data, format='json')
#         return response
#
#     def test_post_and_get_instruktor(self):
#         nowe_imie = 'JanTest'
#         nowe_nazwisko = 'Testowalski'
#         nowa_biografia = 'Lorem_ipsum_dolor_sit_amet'
#         nowy_email = 'test@mail.com'
#         nowy_nick = 'testowy'
#         nowy_slug = 'JanTest_Testowalski'
#         response = self.post_instruktor(nowe_imie, nowe_nazwisko, nowa_biografia, nowy_email, nowy_nick, nowy_slug)
#         print(response.data)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Instruktor.objects.count() == 1
#         assert Instruktor.objects.get().nick == nowy_nick


class KursTests(APITestCase):
    def create_instruktor(self, slug):
        url = reverse(views.InstruktorListView.name)
        data = {'imie': 'JanTest',
                'nazwisko': 'Testowalski',
                'biografia': 'Lorem_ipsum_dolor_sit_amet',
                'email': 'test@mail.com',
                'nick': 'testowy',
                'slug': slug,
                'kursy': []}
        self.client.post(url, data, format='json')

    def post_kurs(self, nazwa, opis, cena, idInstruktora):
        url = reverse(views.KursListView.name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'cena': cena,
                'idInstruktora': idInstruktora,
                'lekcje': []}
        response = self.client.post(url, data, format='json')
        print(response.data)
        return response

    def test_post_and_get_kurs(self):
        self.create_instruktor('JanTest_Testowalski')
        nowa_nazwa = 'Kurs_testowy'
        nowy_opis = 'Treść_opisu_testowego_kursu'
        nowa_cena = 99.99
        nowe_id_instruktora = 'JanTest_Testowalski'
        response = self.post_kurs(nowa_nazwa, nowy_opis, nowa_cena, nowe_id_instruktora)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kurs.objects.count() == 1
        assert Kurs.objects.get().nazwa == nowa_nazwa

    def test_filter_id_instruktora(self):
        self.create_instruktor('Instruktor1')
        self.create_instruktor('Instruktor2')
        self.create_instruktor('Instruktor3')
        self.post_kurs('Kurs1', 'Opis1', 12.3, 'Instruktor1')
        self.post_kurs('Kurs2', 'Opis2', 36, 'Instruktor1')
        self.post_kurs('Kurs3', 'Opis3', 324.23, 'Instruktor2')
        self.post_kurs('Kurs4', 'Opis4', 123, 'Instruktor3')
        self.post_kurs('Kurs5', 'Opis5', 0.5, 'Instruktor3')

        filter_instruktor = {'idInstruktora': 'Instruktor1'}
        url = '{0}?{1}'.format(reverse(views.KursListView.name), urlencode(filter_instruktor))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][0]['nazwa'] == 'Kurs1'


class LekcjaTests(APITestCase):
    def create_instruktor(self):
        url = reverse(views.InstruktorListView.name)
        data = {'imie': 'JanTest',
                'nazwisko': 'Testowalski',
                'biografia': 'Lorem_ipsum_dolor_sit_amet',
                'email': 'test@mail.com',
                'nick': 'testowy',
                'slug': 'JanTest_Testowalski',
                'kursy': []}
        self.client.post(url, data, format='json')

    def create_kurs(self):
        # self.create_instruktor()
        url = reverse(views.KursListView.name)
        data = {'nazwa': 'Kurs_testowy',
                'opis': 'Treść_opisu_testowego_kursu',
                'cena': 99.99,
                'idInstruktora': 'JanTest_Testowalski',
                'lekcje': []}
        response = self.client.post(url, data, format='json')
        print(response.data)

    def post_lekcja(self, nazwa, opis, idKursu, idInstruktora):
        self.create_instruktor()
        self.create_kurs()
        url = reverse(views.LekcjaListView.name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'idKursu': idKursu,
                'idInstruktora': idInstruktora,
                'zasoby': []}
        response = self.client.post(url, data, format='json')
        print(response.data)
        return response

    def test_post_and_get_lekcja(self):
        nowa_nazwa = 'Lekcja_testowa'
        nowy_opis = 'Treść_opisu_testowego_lekcji'
        nowe_id_kursu = 'Kurs_testowy'
        nowe_id_instruktora = 'JanTest_Testowalski'
        response = self.post_lekcja(nowa_nazwa, nowy_opis, nowe_id_kursu, nowe_id_instruktora)
        assert response.status_code == status.HTTP_201_CREATED
        assert Lekcja.objects.count() == 1
        assert Lekcja.objects.get().nazwa == nowa_nazwa
