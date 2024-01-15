from django.contrib import admin
from cardapio.models import Prato

class ListandoPratos(admin.ModelAdmin):
    list_display = ("id", "nome", "foto")
    search_fields = ("nome",)
    list_display_links = ("id", "nome")

# Register your models here.
admin.site.register(Prato, ListandoPratos)
