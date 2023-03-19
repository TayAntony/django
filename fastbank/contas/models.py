from django.db import models
from django.core.validators import MinValueValidator


class Endereco(models.Model):
    ACRE = "AC"
    ALAGOAS = "AL"
    AMAPA = "AP"
    AMAZONAS = "AM"
    BAHIA = "BA"
    CEARA = "CE"
    ESPIRITO_SANTO = "ES"
    GOIAS = "GO"
    MARANHAO = "MA"
    MATO_GROSSO = "MT"
    MATO_GROSSO_SUL = "MS"
    MINAS_GERAIS = "MG"
    PARA = "PA"
    PARANA = "PR"
    PARAIBA = "PB"
    PERNAMBUCO = "PE"
    PAIUI = "PI"
    RIO_DE_JANEIRO = "RJ"
    RIO_GRANDE_NORTE = "RN"
    RIO_GRANDE_SUL = "RS"
    RONDONIA = "RO"
    RORAIMA = "RR"
    SAO_PAULO = "SP"
    SANTA_CATARINA = "SC"
    SERGIPE = "SE"
    TOCANTINS = "TO"
    DISTRITO_FEDERAL = "DF"

    ESTADOS = [
        (ACRE, "Acre"),
        (ALAGOAS, "Alagoas"),
        (AMAPA, "Amapa"),
        (AMAZONAS, "Amazonas"),
        (BAHIA, "Bahia"),
        (CEARA, "Ceara"),
        (ESPIRITO_SANTO, "Espírito Santo"),
        (GOIAS, "Goiás"),
        (MARANHAO, "Maranhão"),
        (MATO_GROSSO, "Mato Grosso"),
        (MATO_GROSSO_SUL, "Mato Grosso do Sul"),
        (MINAS_GERAIS, "Minas Gerais"),
        (PARA, "Pará"),
        (PARANA, "Paraná"),
        (PARAIBA, "Paraíba"),
        (PERNAMBUCO, "Pernambuco"),
        (PAIUI, "Piaui"),
        (RIO_DE_JANEIRO, "Rio de Janeiro"),
        (RIO_GRANDE_NORTE, "Rio Grande do Norte"),
        (RIO_GRANDE_SUL, "Rio Grande do Sul"),
        (RONDONIA, "Rondônia"),
        (RORAIMA, "Roraima"),
        (SAO_PAULO, "São Paulo"),
        (SANTA_CATARINA, "Santa Catarina"),
        (SERGIPE, "Sergipe"),
        (TOCANTINS, "Tocantins"),
        (DISTRITO_FEDERAL, "Distrito Federal"),
    ]

    rua = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=4)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS, default=SAO_PAULO)
    complemento = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = "Endereço"


class Contatos(models.Model):
    numero_telefone = models.IntegerField(max_length=11)
    email = models.EmailField()
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Contatos"


class Tipo_cliente(models.Model):
    PESSOA_FISICA = "F"
    PESSOA_JURIDICA = "J"

    TIPO_CLIENTE = [
        (PESSOA_FISICA, "Pessoa Física"),
        (PESSOA_JURIDICA, "Pessoa Jurídica"),
    ]

    tipo_cliente = models.CharField(
        max_length=1, choices=TIPO_CLIENTE, default=PESSOA_FISICA
    )


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    contatos_cliente = models.ForeignKey(Contatos, on_delete=models.DO_NOTHING)
    tipo_cliente = models.ForeignKey(Tipo_cliente, on_delete=models.DO_NOTHING)
    cpf_cnpj = models.CharField(max_length=20)
    data_nascimento_criacao = models.DateField()

    class Meta:
        verbose_name_plural = "Cliente"


class Conta(models.Model):
    CONTA_CORRENTE = "CC"
    CONTA_SALARIO = "CS"
    CONTA_POUPANCA = "CP"

    TIPO_CONTA = [
        (CONTA_CORRENTE, "Conta Corrente"),
        (CONTA_SALARIO, "Conta Salário"),
        (CONTA_POUPANCA, "Conta Poupança"),
    ]

    tipo_conta = models.CharField(
        max_length=2, choices=TIPO_CONTA, default=CONTA_CORRENTE
    )
    nome_cliente_conta = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    numero_conta = models.IntegerField(max_length=5)
    agencia = models.IntegerField(max_length=4)
    digito = models.IntegerField(max_length=1)
    saldo = models.IntegerField(max_length=10)
    data_criacao = models.DateField(auto_now=True)
    conta_ativa = models.BooleanField()

    class Meta:
        verbose_name_plural = "Conta"

    def __str__(self) -> str:
        return self.numero_conta


class Cartao(models.Model):
    numero_cartao = models.CharField(max_length=20)
    cvv = models.IntegerField(max_length=3)
    data_vencimento = models.DateField()
    nome_titular_cartao = models.CharField(max_length=100)
    conta_cartao = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    cartao_ativo = models.BooleanField()


class Transferencia(models.Model):
    # GANHA DINHEIRO NA CONTA
    TRANSFERENCIA_BANCARIA = "B"
    TRANSFERENCIA_PIX = "P"
    TRANSFERENCIA_TED = "T"

    TIPO_TRANSFERENCIA = [
        (TRANSFERENCIA_BANCARIA, "Tranferência bancária"),
        (TRANSFERENCIA_PIX, "Transferência via Pix"),
        (TRANSFERENCIA_TED, "Transferência via TED"),
    ]
    remetente_transferencia = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    data_transferencia = models.DateField()
    valor_transferencia = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transferencia = models.CharField(
        max_length=1, choices=TIPO_TRANSFERENCIA, default=TRANSFERENCIA_PIX
    )


class Pagamentos(models.Model):
    # PERDE DINHEIRO NA CONTA
    PAGAMENTO_CARTAO = "C"
    PAGAMENTO_BOLETO = "B"
    PAGAMENTO_PIX = "P"

    TIPO_PAGAMENTO = [
        (PAGAMENTO_BOLETO, "Boleto"),
        (PAGAMENTO_CARTAO, "Cartão"),
        (PAGAMENTO_PIX, "Pix"),
    ]

    destinatario_pagamento = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    tipo_pagamento = models.CharField(
        max_length=1, choices=TIPO_PAGAMENTO, default=PAGAMENTO_PIX
    )
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now=True)


class Tipo_transacao(models.Model):
    # aumentou ou diminuiu o saldo da conta

    TIPO_TRANSACAO_LISTA = [("P", Pagamentos), ("T", Transferencia)]

    tipo_transacao = models.CharField(
        max_length=1, choices=TIPO_TRANSACAO_LISTA, default="P"
    )


class Extrato_conta(models.Model):
    # histórico de transações da conta
    extrato_conta = models.ForeignKey(Tipo_transacao, on_delete=models.DO_NOTHING)
