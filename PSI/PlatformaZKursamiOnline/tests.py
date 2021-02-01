from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from . import views
from .models import *
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls

# Create your tests here.


class KursTests(APITestCase):
    def create_instruktor(self, slug, client):
        url = reverse(views.InstruktorListView.name)
        data = {'imie': 'JanTest',
                'nazwisko': 'Testowalski',
                'biografia': 'Lorem_ipsum_dolor_sit_amet',
                'email': 'test@mail.com',
                'nick': 'testowy',
                'slug': slug,
                'kursy': []}
        client.post(url, data, format='json')

    def post_kurs(self, nazwa, opis, cena, idInstruktora, client):
        url = reverse(views.KursListView.name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'cena': cena,
                'idInstruktora': idInstruktora,
                'lekcje': []}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_kurs(self):
        User.objects.create_superuser('admin', 'admin@test.com', 'adminTest')
        client = APIClient()
        client.login(username='admin', password='adminTest')
        self.create_instruktor('JanTest_Testowalski', client)
        nowa_nazwa = 'Kurs_testowy'
        nowy_opis = 'Treść_opisu_testowego_kursu'
        nowa_cena = 99.99
        nowe_id_instruktora = 'JanTest_Testowalski'
        response = self.post_kurs(nowa_nazwa, nowy_opis, nowa_cena, nowe_id_instruktora, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kurs.objects.count() == 1
        assert Kurs.objects.get().nazwa == nowa_nazwa

    def test_filter_id_instruktora(self):
        User.objects.create_superuser('admin', 'admin@test.com', 'adminTest')
        client = APIClient()
        client.login(username='admin', password='adminTest')
        self.create_instruktor('Instruktor1', client)
        self.create_instruktor('Instruktor2', client)
        self.create_instruktor('Instruktor3', client)
        self.post_kurs('Kurs1', 'Opis1', 12.3, 'Instruktor1', client)
        self.post_kurs('Kurs2', 'Opis2', 36, 'Instruktor1', client)
        self.post_kurs('Kurs3', 'Opis3', 324.23, 'Instruktor2', client)
        self.post_kurs('Kurs4', 'Opis4', 123, 'Instruktor3', client)
        self.post_kurs('Kurs5', 'Opis5', 0.5, 'Instruktor3', client)

        filter_instruktor = {'idInstruktora': 'Instruktor1'}
        url = '{0}?{1}'.format(reverse(views.KursListView.name), urlencode(filter_instruktor))
        response = client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][0]['nazwa'] == 'Kurs1'


class LekcjaTests(APITestCase):
    def create_instruktor(self, client):
        url = reverse(views.InstruktorListView.name)
        data = {'imie': 'JanTest',
                'nazwisko': 'Testowalski',
                'biografia': 'Lorem_ipsum_dolor_sit_amet',
                'email': 'test@mail.com',
                'nick': 'testowy',
                'slug': 'JanTest_Testowalski',
                'kursy': []}
        client.post(url, data, format='json')

    def create_kurs(self, client):
        url = reverse(views.KursListView.name)
        data = {'nazwa': 'Kurs_testowy',
                'opis': 'Treść_opisu_testowego_kursu',
                'cena': 99.99,
                'idInstruktora': 'JanTest_Testowalski',
                'lekcje': []}
        client.post(url, data, format='json')

    def post_lekcja(self, nazwa, opis, idKursu, idInstruktora, client):
        self.create_instruktor(client)
        self.create_kurs(client)
        url = reverse(views.LekcjaListView.name)
        data = {'nazwa': nazwa,
                'opis': opis,
                'idKursu': idKursu,
                'idInstruktora': idInstruktora,
                'zasoby': []}
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_lekcja(self):
        User.objects.create_superuser('admin', 'admin@test.com', 'adminTest')
        client = APIClient()
        client.login(username='admin', password='adminTest')
        nowa_nazwa = 'Lekcja_testowa'
        nowy_opis = 'Treść_opisu_testowego_lekcji'
        nowe_id_kursu = 'Kurs_testowy'
        nowe_id_instruktora = 'JanTest_Testowalski'
        response = self.post_lekcja(nowa_nazwa, nowy_opis, nowe_id_kursu, nowe_id_instruktora, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Lekcja.objects.count() == 1
        assert Lekcja.objects.get().nazwa == nowa_nazwa

    def test_update_and_get_lekcja(self):
        User.objects.create_superuser('admin', 'admin@test.com', 'adminTest')
        client = APIClient()
        client.login(username='admin', password='adminTest')
        nowa_nazwa = 'Lekcja_testowa'
        nowy_opis = 'Treść_opisu_testowego_lekcji'
        nowe_id_kursu = 'Kurs_testowy'
        nowe_id_instruktora = 'JanTest_Testowalski'
        response = self.post_lekcja(nowa_nazwa, nowy_opis, nowe_id_kursu, nowe_id_instruktora, client)
        url = urls.reverse(views.LekcjaDetailView.name, None, {response.data['id']})
        zmieniony_opis = 'Zmiana opisu'
        data = {'opis': zmieniony_opis}
        patch_response = client.patch(url, data, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['opis'] == zmieniony_opis
