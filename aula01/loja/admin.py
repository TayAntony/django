from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Categorias)
@admin.register(models.Produtos)

class ProdutoAdmin (admin.ModelAdmin):
    list_display = ['nome', 'preco', 'qtd_estoque', 'validade', 'disponibilidade']
    search_fields = ['nome']

admin.site.register(models.Clientes)
