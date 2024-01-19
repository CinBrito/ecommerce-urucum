from django.contrib import admin
from perfil.models import Cliente

# Register your models here.
class ListandoClientes(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone", "bairro")
    search_fields = ("nome","email", "telefone")
    list_display_links = ("id", "nome")

# Register your models here.
admin.site.register(Cliente, ListandoClientes)