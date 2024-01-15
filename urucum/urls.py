from django.urls import path
from urucum.views import index, duvidas

urlpatterns = [
    path('', index, name='index'),
    path('duvidas/', duvidas, name='duvidas')
]