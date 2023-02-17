from django.db import models
from django.core.validators import MinValueValidator

class Categorias(models.Model):
    nome_modelo = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self) -> str:
        return self.nome_modelo
    
class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.IntegerField(validators=[MinValueValidator (1, message= "A quantidade no estoque deve ser maior que 0")])
    descricao = models.TextField()
    disponibilidade = models.BooleanField()
    categoria_prod = models.ForeignKey(Categorias, on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = 'Produtos'
    
    def __str__(self) -> str:
        return self.nome
    
class Clientes(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self) -> str:
        return self.nome
    
    
    
class Vendas(models.Model):
    TIPO_PAGAMENTO = [
            ('B', 'Boleto'),
            ('C', 'Cartão crédito'),
            ('D', 'Cartão débito'),
            ('P', 'Pix')
        ]
    ESTADO_PAGAMENTO = [
        ('A', 'Aprovado'),
        ('R', 'Recusado'),
        ('P', 'Processamento/Pendente')
    ]

    preco_total = models.DecimalField(max_digits=8, decimal_places=2)
    estado_pagamento = models.CharField(max_length=1, choices=ESTADO_PAGAMENTO, default='P')
    tipo_pagamento = models.CharField(max_length=1, choices=TIPO_PAGAMENTO, default='P')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Vendas'

class Pedidos(models.Model):
    produto_fk = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    pedido_fk = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    preco_atual = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Pedidos'
