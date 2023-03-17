from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id',  'rua', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'complemento')

@admin.register(models.Contatos)
class ContatosClienteAdmin(admin.ModelAdmin):
    list_display=('numero_telefone', 'email','endereco')

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'contatos_cliente', 'tipo_cliente', 'cpf_cnpj', 'data_nascimento_criacao')

@admin.register(models.Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente_conta', 'numero_conta', 'agencia', 'digito', 'saldo', 'data_criacao', 'tipo_conta')

@admin.register(models.Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_titular_cartao' ,'numero_cartao', 'cvv', 'data_vencimento', 'conta_cartao','cartao_ativo')


@admin.register(models.Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'remetente_transferencia', 'data_transferencia', 'valor_transferencia', 'tipo_transferencia')

@admin.register(models.Pagamentos)
class PagamentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'destinatario_pagamento', 'data_pagamento', 'valor_pagamento', 'tipo_pagamento')
