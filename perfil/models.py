from django.db import models
from django.forms import ModelForm


# Create your models here.

class Cliente(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    sobrenome = models.CharField(max_length=150, null=False, blank=False)
    # senha = PESQUISAR
    telefone = models.CharField(max_length=13, null=False, blank=False)
    endereco = models.CharField(max_length=500, null=False, blank=False)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cep = models.CharField(max_length=9)
    status = models.BooleanField(default=False)

# class ClienteForm(ModelForm):
#    class Meta:
#        model = Cliente
#        fields = ["nome","sobrenome","email","endereco","complemento","bairro","cep"]
