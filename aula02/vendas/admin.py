from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Categorias)

@admin.register(models.Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ['nome', 'preco', 'qtd_estoque']

@admin.register(models.Clientes)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(models.Vendas)
class VendasAdmin(admin.ModelAdmin):
    list_display = ['estado_pagamento', 'data_venda']

@admin.register(models.Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ['produto_fk', 'preco_atual', 'quantidade']