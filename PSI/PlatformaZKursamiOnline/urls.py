from django.urls import path
from . import views

app_name = 'PlatformaZKursamiOnline'

urlpatterns = [
    path('', views.default, name='default'),
]
