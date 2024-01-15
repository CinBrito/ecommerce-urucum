from django.db import models

# Create your models here.
class Prato(models.Model):

    # OPCOES_CATEGORIA = [
    #     ("NEBULOSA","Nebulosa"),
    #     ("ESTRELA", "Estrela"),
    #     ("GALÁXIA", "Galáxia"),
    #     ("PLANETA", "Planeta")
    # ]

    nome = models.CharField(max_length=500, null=False, blank=False)
    # categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
    calorias = models.IntegerField(null=False, blank=False)
    carbo = models.IntegerField(null=False, blank=False)
    gorduras = models.IntegerField(null=False, blank=False)
    proteinas = models.IntegerField(null=False, blank=False)
    valor = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Prato: [nome={self.nome}]"