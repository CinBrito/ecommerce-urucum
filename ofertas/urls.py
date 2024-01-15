from django.urls import path
from ofertas.views import ofertas

urlpatterns = [
    path('ofertas/', ofertas, name='ofertas')
]