from django.shortcuts import render
from urucum.models import Prato

def index(request):
    pratos = Prato.objects.filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": pratos})
    pratos = Prato.objects.filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": pratos})

def duvidas(request):
    return render(request, 'galeria/duvidas.html')
