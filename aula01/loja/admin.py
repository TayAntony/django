from django.contrib import admin, messages
from . import models


admin.site.register(models.Categorias)
@admin.register(models.Produtos)


class ProdutoAdmin (admin.ModelAdmin):
   
    list_display = ['nome', 'preco', 'qtd_estoque', 'validade', 'disponibilidade']
    actions = ['zerar_estoque']

    @admin.action(description='Preço aumentado em 30%%')
    def aumentar_preco(self, request, queryset):
        for produto in queryset:
            produto_atualizado = produto.
            
        self.message_user(request, f'{produto_atualizado} produtos foram atualizados!', messages.SUCCESS)

    @admin.action(description='Zerar estoque')
    def zerar_estoque(self, request, queryset):
        print(queryset)
        total_atualizado = queryset.update(qtd_estoque=0)
        self.message_user(request, f'{total_atualizado} produtos foram atualizados!', messages.WARNING)
    


@admin.register(models.Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipoCliente']
    list_editable = ['nome', 'tipoCliente']
    list_filter = ['tipoCliente']
    