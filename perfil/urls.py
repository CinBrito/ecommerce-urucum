from django.urls import path
from perfil.views import perfil, meuperfil

urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('meuperfil/', meuperfil, name='meuperfil')
]