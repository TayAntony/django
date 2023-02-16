from django.contrib import admin, messages
from . import models
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.db.models import QuerySet

admin.site.register(models.Categorias)

class EstoqueFiltro(admin.SimpleListFilter):
    title = "Filter"
    parameter_name = "avaliar_estoque"

    def lookups(self, request, model_admin):
        return [
            ("Estoque zerado", "Estoque zerado"),
            ("Estoque baixo", "Estoque baixo"),
            ("Estoque OK", "Estoque OK"),
            ("Estoque alto", "Estoque alto")
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "Estoque zerado":
            #SELECT * FROM QTD_ESTOQUE WHERE QTD_ESTOQUE == 0
            return queryset.filter(
                qtd_estoque=0
            )
        if self.value() == "Estoque baixo":
            return queryset.filter(
                qtd_estoque__gte=1,
                qtd_estoque__lte=10,
            )
        if self.value() == "Estoque OK":
            return queryset.filter(
                qtd_estoque__gte=11,
                qtd_estoque__lte=30)
        if self.value() == "Estoque alto":
            return queryset.filter(
                qtd_estoque__gte=30
            )
        
@admin.register(models.Produtos)
class ProdutoAdmin (admin.ModelAdmin):
    list_display = ['nome', 'preco', 'qtd_estoque', 'validade', 'disponibilidade', 'avaliar_estoque']
    actions = ['zerar_estoque', 'aumentar_preco', 'diminuir_preco']
    list_filter = ['disponibilidade', EstoqueFiltro]
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
            preco_atual = float(preco_antigo) - preco_atual
            total_atualizado = queryset.update(preco=preco_atual)
            print(total_atualizado)

        self.message_user(request, f'{total_atualizado} produtos foram atualizados!', messages.SUCCESS)

    @admin.display(ordering='qtd')
    def avaliar_estoque(self, produto):
        if produto.qtd_estoque < 0:
            produto.qtd_estoque = 0
            produto.save()
        elif produto.qtd_estoque > 30:
            return 'Estoque alto'
        elif produto.qtd_estoque >=10:
            return 'Estoque OK'
        elif produto.qtd_estoque == 0:
            return 'Estoque zerado'
        else:
            return 'Estoque baixo'


@admin.register(models.Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipoCliente']
    list_editable = ['nome', 'tipoCliente']
    list_filter = ['tipoCliente']
    