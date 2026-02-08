from django.urls import path
from .views import *
from .views import home_view

app_name = 'synergia'
"""
path(
path('rota/',
path('rota/', nome_da_funcao_view,
path('rota/', nome_da_funcao_view, name='nome-dessa-url')
"""
# tipo: <form  method="post" action="{% url 'app:nome-dessa-url' %}">
urlpatterns = [
    path('', home_view, name='home'),
    path('Criador-Poderes/', criador_poderes_view, name='criador-poderes'),
]