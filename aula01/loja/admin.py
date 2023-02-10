from django.contrib import admin, messages
from . import models


admin.site.register(models.Categorias)
@admin.register(models.Produtos)


class ProdutoAdmin (admin.ModelAdmin):
    list_display = ['nome', 'preco', 'qtd_estoque', 'validade', 'disponibilidade', 'avaliar_estoque']
    actions = ['zerar_estoque', 'aumentar_preco', 'diminuir_preco']
    list_filter = ['qtd_estoque', 'disponibilidade']
    search_fields = ['nome__istartswith']
    list_editable = ['qtd_estoque']
    

    @admin.action(description= 'Preço aumentado em 30%%')
    def aumentar_preco(self, request, queryset):
        total_produtos = len(queryset)
        for produto in queryset:
            preco_antigo = float(produto.preco)
            preco_atual = preco_antigo * 0.3
            preco_atual += preco_antigo
            produto.preco = preco_atual
            produto.save()

        self.message_user(request, f'{total_produtos} produtos foram atualizados!', messages.SUCCESS)

    @admin.action(description='Zerar estoque')
    def zerar_estoque(self, request, queryset):
        print(queryset)
        total_atualizado = queryset.update(qtd_estoque=0)

        self.message_user(request, f'{total_atualizado} produtos foram atualizados!', messages.WARNING)
    

    @admin.action(description= 'Preço diminuido em 30%%')
    def diminuir_preco(self, request, queryset):
        for produto in queryset:
            preco_antigo = produto.preco
            preco_atual = float(preco_antigo) * 0.3
            preco_atual -= float(preco_antigo)
            total_atualizado = queryset.update(preco=preco_atual)
            print(total_atualizado)

        self.message_user(request, f'{total_atualizado} produtos foram atualizados!', messages.SUCCESS)

    def avaliar_estoque(self, produto):
        if produto.qtd_estoque < 0:
            produto.qtd_estoque = 0
            produto.save()
        elif produto.qtd_estoque >=10:
            return 'Estoque OK'
        elif produto.qtd_estoque == 0:
            return 'Estoque zerado'
        elif produto.qtd_estoque > 30:
            return 'Estoque alto'
        else:
            return 'Estoque baixo'


@admin.register(models.Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipoCliente']
    list_editable = ['nome', 'tipoCliente']
    list_filter = ['tipoCliente']
    