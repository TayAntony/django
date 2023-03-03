from django.shortcuts import render
from .models import Produtos, Clientes, Categorias, PedidoCompleto, ItemPedido
from .serializer import ClienteSerializer, CategoriaSerializer, ProdutosSerializer,PedidoCompletoSerializer, ItemPedidoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes


#===================      MODEL CLIENTE     =============================================
def listar_clientes(request):
    if request.method == 'GET':
        # Armazena os resultados da query
        queryset = Clientes.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(['GET', 'DELETE', 'PUT'])
def detalhe_cliente(request, id):
    try:
        cliente = Clientes.objects.get(pk=id)
    except Clientes.DoesNotExist:
        return Response('Cliente não encontrado', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Cliente atualizado', serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        cliente.delete()
        return Response('Cliente deletado',status=status.HTTP_204_NO_CONTENT)


#===================      MODEL CATEGORIAS     =============================================
def listar_categorias(request):
    if request.method == 'GET':
        categorias = Categorias.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(['GET', 'DELETE', 'PUT'])
def detalhe_categoria(request, id):
    try:
        categoria = Categorias.objects.get(pk=id)
    except Categorias.DoesNotExist:
        return Response('Categoria não encontrada', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Categoria atualizada', serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        categoria.delete()
        return Response('Categoria deletada',status=status.HTTP_204_NO_CONTENT)


#===================      MODEL PRODUTOS     =============================================
def listar_produtos(request):
    if request.method == 'GET':
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = ProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(['GET', 'DELETE', 'PUT'])
def detalhe_produto(request, id):
    try:
        produto = Produtos.objects.get(pk=id)
    except Produtos.DoesNotExist:
        return Response('Produto não encontrado', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProdutosSerializer(produto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProdutosSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Produto atualizado', serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        produto.delete()
        return Response('Produto deletado',status=status.HTTP_204_NO_CONTENT)
    
#===================      MODEL PEDIDOS     =============================================
def listar_pedido_completo(request):
    if request.method == 'GET':
        pedido_completo = PedidoCompleto.objects.all()
        serializer = PedidoCompletoSerializer(pedido_completo, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = PedidoCompletoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(['GET', 'DELETE', 'PUT'])
def detalhe_pedido_completo(request, id):
    try:
        pedidos_completos = PedidoCompleto.objects.get(pk=id)
    except PedidoCompleto.DoesNotExist:
        return Response('Pedido não encontrado', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PedidoCompletoSerializer(pedidos_completos)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PedidoCompletoSerializer(pedidos_completos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Pedido atualizado', serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        pedidos_completos.delete()
        return Response('Pedido deletado',status=status.HTTP_204_NO_CONTENT)
    
#===================      MODEL ITEMPEDIDO     =============================================
def listar_item_pedido(request):
    if request.method == 'GET':
        item_pedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(item_pedido, many=True)
        return Response(serializer.data)    
    
    elif request.method == 'POST':
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(['GET', 'DELETE', 'PUT'])
def detalhe_item_pedido(request, id):
    try:
        itens_pedidos = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        return Response('Item do pedido não encontrado', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemPedidoSerializer(itens_pedidos)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItemPedidoSerializer(itens_pedidos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Item do pedido atualizado', serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        itens_pedidos.delete()
        return Response('Item do pedido deletado',status=status.HTTP_204_NO_CONTENT)