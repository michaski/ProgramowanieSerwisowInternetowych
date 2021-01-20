from django.urls import path
from . import views

# app_name = 'PlatformaZKursamiOnline'

urlpatterns = [
    path('kursy/', views.KursListView.as_view(), name=views.KursListView.name),
    path('kursy/<pk>/', views.KursDetailView.as_view(), name=views.KursDetailView.name),
    path('lekcje/', views.LekcjaListView.as_view(), name='lista_lekcji'),
    path('lekcje/<pk>/', views.LekcjaDetailView.as_view(), name='informacje_o_lekcji'),
    path('zasoby/', views.ZasobListView.as_view(), name='lista_zasobow'),
    path('platnosci/', views.PlatnoscListView.as_view(), name='lista_platnosci'),
    path('instruktorzy/', views.InstruktorListView.as_view(), name='lista_instuktorow'),
    path('instruktorzy/<pk>/', views.InstruktorDetailView.as_view(), name='informacje_o_instruktorze'),
    path('uzytkownicy/', views.UzytkownikListView.as_view(), name='lista_uzytkownikow'),
    path('uzytkownicy/<pk>/', views.UzytkownikDetailView.as_view(), name='informacje_o_uzytkowniku'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
