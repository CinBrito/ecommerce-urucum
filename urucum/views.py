from django.shortcuts import render

def index(request):
    """Dicionário chamado dados"""
    dados = {
        '1': {
            "nome": "Salada de Quinoa & Grão-de-Bico com Cogumelos",
              "legenda": "Descrição Descrição Descrição"},
        '2': {
            "nome": "Dahl com Lentilhas Vermelhas & Arroz",
              "legenda": "Descrição Descrição Descrição"},
        '3': {
            "nome": "Chana Masala com Coentro, Caju & Arroz",
              "legenda": "Descrição Descrição Descrição"},
        '4': {
            "nome": "Guisado de Tofu, Tomate & Pimentão com Arroz",
              "legenda": "Descrição Descrição Descrição"}

    }

    return render(request, 'galeria/index.html', )

def duvidas(request):
    return render(request, 'galeria/duvidas.html')
