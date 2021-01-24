from django.urls import path
from . import views

# app_name = 'PlatformaZKursamiOnline'

urlpatterns = [
    path('kursy/', views.KursListView.as_view(), name=views.KursListView.name),
    path('kursy/<pk>/', views.KursDetailView.as_view(), name=views.KursDetailView.name),
    path('lekcje/', views.LekcjaListView.as_view(), name=views.LekcjaListView.name),
    path('lekcje/<pk>/', views.LekcjaDetailView.as_view(), name=views.LekcjaDetailView.name),
    path('zasoby/', views.ZasobListView.as_view(), name=views.ZasobListView.name),
    path('zasoby/<pk>/', views.ZasobDetailView.as_view(), name=views.ZasobDetailView.name),
    path('platnosci/', views.PlatnoscListView.as_view(), name=views.PlatnoscListView.name),
    path('instruktorzy/', views.InstruktorListView.as_view(), name=views.InstruktorListView.name),
    path('instruktorzy/<pk>/', views.InstruktorDetailView.as_view(), name=views.InstruktorDetailView.name),
    path('uzytkownicy/', views.UzytkownikListView.as_view(), name=views.UzytkownikListView.name),
    path('uzytkownicy/<pk>/', views.UzytkownikDetailView.as_view(), name=views.UzytkownikDetailView.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
