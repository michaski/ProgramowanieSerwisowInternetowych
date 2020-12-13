from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


def default(request):
    return render(request, 'default.html')


