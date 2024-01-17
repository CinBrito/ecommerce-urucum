from django.shortcuts import render
from cardapio.models import Prato

def cardapio(request):
    pratos = Prato.objects.filter(publicado=True)
    return render(request, 'galeria/cardapio.html', {"cards": pratos})
