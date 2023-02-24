from django.contrib import admin
from . import models
import decimal

#TODO DIMINUIR O ESTOQUE E IMPEDIR COMPRA SE NÃO TIVER ESTOQUE SUFICIENTE
#TODO NAO DEIXAR O CAMPO PREÇO TOTAL EDITÁVEL NOS PEDIDOS (E MOSTRAR A CONTA DO PREÇO TOTAL DA COMPRA)

admin.site.register(models.Categorias)

@admin.register(models.Clientes)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(models.Produtos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ['id','nome', 'preco', 'qtd_estoque', 'disponibilidade']


class PedidoItemInline(admin.TabularInline):
    model = models.ItemPedido
    readonly_fields = ['preco_atual', 'total_pagamento']

@admin.register(models.PedidoCompleto)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'estado_pagamento', 'estado_pedido','data_venda', 'preco_total', 'cliente']
    inlines = [
       PedidoItemInline
    ]

    def save_formset(self, request, form, formset, change) -> None:
        instances = formset.save(commit=False)
        for instance in instances:
            instance.preco_atual = instance.produto.preco
            instance.total_pagamento = instance.quantidade * instance.preco_atual
            instance.save()

        return super().save_formset(request, form, formset, change)
