from django.shortcuts import get_object_or_404, render
from .models import Produtos, Clientes, Categorias, PedidoCompleto, ItemPedido
from .serializer import ClienteSerializer, CategoriaSerializer, ProdutosSerializer,PedidoCompletoSerializer, ItemPedidoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#---------- LISTAR E DETALHAR CLIENTE --------------
class ListarClientes(ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

class DetalharClientes(RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

#---------- LISTAR E DETALHAR PRODUTOS --------------
class ListarProdutos(ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class DetalharProdutos(RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

    def delete(self, request, *args, **kwargs):
        produto = get_object_or_404(Produtos, pk=kwargs['pk'])
        if produto.qtd_estoque > 0 and produto.disponibilidade:
            return Response({'message':"Não é possível excluir pois ainda existe no estoque."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().delete(request, *args, **kwargs)

#---------- LISTAR E DETALHAR CATEGORIAS --------------
class ListarCategorias(ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

class DetalharCategorias(RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerializer

#---------- LISTAR E DETALHAR PEDIDOS --------------
class ListarPedidoCompleto(ListCreateAPIView):
    queryset = PedidoCompleto.objects.all()
    serializer_class = CategoriaSerializer

class DetalharPedidoCompleto(RetrieveUpdateDestroyAPIView):
    queryset = PedidoCompleto.objects.all()
    serializer_class = PedidoCompletoSerializer


#---------- LISTAR E DETALHAR ITEMPEDIDO --------------
class ListarItemPedido(ListCreateAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

class DetalharItemPedido(RetrieveUpdateDestroyAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

    def addItem(self, item, quantidade):
        estoque = ItemPedido.objects.get(item=item)
        estoque.quantidade += quantidade
        estoque.save()

    def subItem(self, item, quantidade):
        estoque = ItemPedido.objects.get(item=item)
        estoque.quantidade -= quantidade
        estoque.save()