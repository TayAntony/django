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
       


class PedidoCompleto(models.Model):
    PAGAMENTO_CREDITO = 'C'
    PAGAMENTO_DEBITO = 'D'
    PAGAMENTO_BOLETO = 'B'
    PAGAMENTO_PIX = 'P'
    TIPO_PAGAMENTO = [
            (PAGAMENTO_BOLETO, 'Boleto'),
            (PAGAMENTO_CREDITO, 'Cartão crédito'),
            (PAGAMENTO_DEBITO, 'Cartão débito'),
            (PAGAMENTO_PIX, 'Pix')
        ]
    
    PAGAMENTO_APROVADO = 'A'
    PAGAMENTO_RECUSADO = 'R'
    PAGAMENTO_PENDENTE = 'P'
    ESTADO_PAGAMENTO = [
        (PAGAMENTO_APROVADO, 'Aprovado'),
        (PAGAMENTO_RECUSADO, 'Recusado'),
        (PAGAMENTO_PENDENTE, 'Processamento/Pendente')
    ]

    ENTREGA_CAMINHO = 'C'
    ENTREGA_ENTREGUE = 'E'
    ENTREGA_PREPARACAO = 'P'
    ENTREGA_CANCELADA = 'X'
    ENTREGA_AGUARDANDO = 'A'
    ESTADO_ENTREGA = [
        (ENTREGA_CAMINHO, 'À caminho'),
        (ENTREGA_ENTREGUE, 'Entregue'),
        (ENTREGA_PREPARACAO, 'Em preparação'),
        (ENTREGA_CANCELADA, 'Cancelado'),
        (ENTREGA_AGUARDANDO, 'Aguardando'),
    ]

    
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)

    estado_pagamento = models.CharField(max_length=1, choices=ESTADO_PAGAMENTO, default=PAGAMENTO_PENDENTE)
    tipo_pagamento = models.CharField(max_length=1, choices=TIPO_PAGAMENTO, default=PAGAMENTO_PIX)
    estado_pedido = models.CharField(max_length=1, choices=ESTADO_ENTREGA, default=ENTREGA_AGUARDANDO)

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return str(self.id) + " - " + self.cliente.nome

class ItemPedido(models.Model):
    preco_atual = models.DecimalField(max_digits=6, decimal_places=2)
    pedido = models.ForeignKey(PedidoCompleto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(validators=[MinValueValidator (1, message= "A quantidade deve ser maior ou igual a 1")])
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    total_pagamento = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Item Pedido'

    
