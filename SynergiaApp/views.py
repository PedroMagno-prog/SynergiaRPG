from django.shortcuts import render
from .util import *

def home_view(request):
    return render(request, 'pages/home.html', {'title': 'Home'})

def criador_poderes_view(request):
    return render(request, 'pages/criador-poderes.html')

