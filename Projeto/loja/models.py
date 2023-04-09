from django.db import models

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=50)
    codigo_hex = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveIntegerField()
    disponibilidade = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="produtos")
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    num_parcelas = models.PositiveIntegerField(default=True)
    vendedora = models.CharField(max_length=50, default='Magazine')

    cores = models.ManyToManyField(Cor)
    #SELECT * FROM PRODUTOS INNER JOIN CATEGORIAS
    #ON PRODUTOS.IDCATEGORIA = CATEGORIAS.ID
    #10 - Coca Cola - 5.00 - 10 - Refrigerante - 3
    #PEDIDOITEM IDPRODUTO = 10

    #PEDIDOS
    #PEDIDOS_ITENS
    #PEDIDOS_ENTREGAS


class Clientes(models.Model):
    avaliacao = models.ForeignKey(Produtos, on_delete=models.PROTECT, default='5')
    foto = models.ImageField(upload_to="cliente", default='foto.png')
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    data_cadastro = models.DateField(auto_now=True)

class Enderecos(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

class Pedidos(models.Model):
    STATUS_PAGAMENTO_PENDENTE = 'P'
    STATUS_PAGAMENTO_APROVADO = 'A'
    STATUS_PAGAMENTO_NEGADO = 'N'

    LISTA_STATUS_PAGAMENTO = [
        (STATUS_PAGAMENTO_PENDENTE, 'Pendente'),
        (STATUS_PAGAMENTO_APROVADO, 'Aprovado'),
        (STATUS_PAGAMENTO_NEGADO, 'Negado'),
    ]

    STATUS_PEDIDO_CANCELADO = 'C'
    STATUS_PEDIDO_ENTREGUE = 'E'
    STATUS_PEDIDO_PREPARACAO = 'P'
    STATUS_PEDIDO_AGUARDANDO = 'A'
    STATUS_PEDIDO_TRANSPORTE = 'T'

    LISTA_STATUS_PEDIDO = [
        (STATUS_PEDIDO_CANCELADO, 'Cancelado'),
        (STATUS_PEDIDO_ENTREGUE, 'Entregue'),
        (STATUS_PEDIDO_PREPARACAO, 'Preparação'),
        (STATUS_PEDIDO_AGUARDANDO, 'Aguardando'),
        (STATUS_PEDIDO_TRANSPORTE, 'Transporte'),
    ]

    PAGAMENTO_PIX = 'P'
    PAGAMENTO_BOLETO = 'B'
    PAGAMENTO_CARTAO = 'C'
    LISTA_PAGAMENTO = [
        (PAGAMENTO_PIX, 'Pix'),
        (PAGAMENTO_BOLETO, 'Boleto'),
        (PAGAMENTO_CARTAO, 'Cartão'),
    ]

    metodo = models.CharField(max_length=1, choices=LISTA_PAGAMENTO, default=PAGAMENTO_PIX)

    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    endereco = models.ForeignKey(Enderecos, on_delete=models.PROTECT)
    data_pedido = models.DateField(auto_now=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status_pagamento = models.CharField(max_length=1, choices=LISTA_STATUS_PAGAMENTO, default=STATUS_PAGAMENTO_PENDENTE)
    status_pedido = models.CharField(max_length=1, choices=LISTA_STATUS_PEDIDO, default=STATUS_PEDIDO_AGUARDANDO)


class PedidosItens(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE )

class Comentario(models.Model):
    avaliacao_produto = models.ForeignKey(Produtos, on_delete=models.PROTECT, default='5')
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT )
    titulo_comentario = models.CharField(max_length=20)
    comentario = models.TextField()
