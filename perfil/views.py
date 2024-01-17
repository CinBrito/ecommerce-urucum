from django.shortcuts import render

def perfil(request):
    return render(request, 'galeria/perfil.html')

def meuperfil(request):
    return render(request, 'galeria/meuperfil.html')
