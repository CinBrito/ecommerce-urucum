from django.contrib import admin
from perfil.models import Cliente


class ListandoClientes(admin.ModelAdmin):
    list_display = ("id", "nome","sobrenome","email","bairro")
    search_fields = ("nome","telefone","email")
    list_display_links = ("id", "nome")
    list_per_page = 10

# Register your models here.
admin.site.register(Cliente, ListandoClientes)
