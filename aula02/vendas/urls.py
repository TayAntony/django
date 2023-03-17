from django.urls import path
from . import views


urlpatterns = [
    path("clientes/", view = views.ListarClientes.as_view()),
    path("cliente-id/<int:pk>", view = views.DetalharClientes.as_view()),
    path("categorias/", view = views.ListarCategorias.as_view()),
    path("categorias-id/<int:pk>", view = views.DetalharCategorias.as_view()),
    path("produtos/", view = views.ListarProdutos.as_view()),
    path("produtos-id/<int:pk>", view = views.DetalharProdutos.as_view()),
    path("pedidos/", view = views.ListarPedidoCompleto.as_view()),
    path("pedidos-id/<int:pk>", view = views.DetalharPedidoCompleto.as_view()),
    path("itempedido/", view = views.ListarItemPedido.as_view()),
    path("itempedido-id/<int:pk>", view = views.DetalharItemPedido.as_view()),
]
