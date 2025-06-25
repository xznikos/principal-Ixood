from django.db import models

class EncomendasModel(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='encomendas_imagens/', null=True, blank=True)
    
    def __str__(self):
        return self.nome
# Create your models here.
