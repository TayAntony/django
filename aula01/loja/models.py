from django.db import models

class Categorias(models.Model):
    nome_modelo = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'

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

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

class Clientes(models.Model):
    CLIENTE_FREE = 'F'
    CLIENTE_PREMIUM = 'P'
    CLIENTE_MASTER = 'M'

    TIPOS_CLIENTES = [
        ('F', 'Free'),
        ('P', 'Premium'),
        ('M', 'Master')
    ]
    nome= models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14)
    resumo = models.TextField()
    dataNascimento = models.DateField()
    dataCadastro = models.DateField(auto_now=True)
    tipoCliente = models.CharField(max_length=1, choices=TIPOS_CLIENTES, default='F')

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self) -> str:
        return self.nome