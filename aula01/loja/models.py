from django.db import models


class Categorias(models.Model):
    nome_modelo = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nome_modelo

class Produtos (models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.IntegerField()
    descricao = models.TextField()
    validade = models.DateField()
    disponibilidade = models.BooleanField()

    categoria_prod = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Clientes(models.Model):
    nome= models.CharField(max_length=255)
    resumo = models.TextField()
    
    def __str__(self) -> str:
        return self.nome