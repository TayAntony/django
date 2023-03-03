from rest_framework import serializers
from .models import Clientes, Produtos, Categorias,PedidoCompleto, ItemPedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clientes
        fields = ['id', 'nome', 'email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categorias
        fields = ['nome_modelo']

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Produtos
        fields = ['nome', 'preco', 'qtd_estoque', 'descricao', 'disponibilidade', 'categoria_prod']
    
class PedidoCompletoSerializer(serializers.ModelSerializer):
    class Meta:
        model= PedidoCompleto
        fields = ['nome', 'preco', 'qtd_estoque', 'descricao', 'disponibilidade', 'categoria_prod']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ItemPedido
        fields = ['preco_atual', 'pedido', 'quantidade', 'produto']