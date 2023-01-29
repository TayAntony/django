from django.db import models

class Produtos (models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Clientes(models.Model):
    nome= models.CharField(max_length=255)
    resumo = models.TextField()
    
    def __str__(self) -> str:
        return self.nome