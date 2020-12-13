from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Uzytkownik)
admin.site.register(Instruktor)
admin.site.register(Kurs)
admin.site.register(Lekcja)
admin.site.register(Zasob)
admin.site.register(Platnosc)

