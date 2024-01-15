from django.urls import path
from cardapio.views import cardapio

urlpatterns = [
    path('cardapio/', cardapio, name='cardapio'),
]