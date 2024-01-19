from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)    
    email = models.EmailField(max_length=254, null=False, blank=False)
    telefone = models.CharField(max_length=13, null=False, blank=False)
    #senha ???
    endereco = models.CharField(max_length=254, null=False, blank=False)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cep = models.CharField(max_length=9)

    
    def __str__(self):
        return f"Cliente: [nome={self.nome}]\nTelefone: [telefone={self.telefone}]"

    

