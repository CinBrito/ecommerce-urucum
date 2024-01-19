from django.contrib import admin
from urucum.models import Prato

class ListandoPratos(admin.ModelAdmin):
    list_display = ("id", "nome", "foto", "categoria","publicado")
    search_fields = ("nome","categoria")
    list_display_links = ("id", "nome")
    list_per_page = 10
    list_editable = ("publicado",)

# Register your models here.

admin.site.register(Prato, ListandoPratos)
