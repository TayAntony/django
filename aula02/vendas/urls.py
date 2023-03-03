from django.urls import path
from . import views


urlpatterns = [
    path("clientes/", views.listar_clientes),
    path("clientes/<int:id>", views.detalhe_cliente),
    path("categorias/", view = views.listar_categorias),
    path("categorias/<int:id>", view = views.detalhe_categoria),
    path("produtos/", view = views.listar_produtos),
    path("produtos/<int:id>", view = views.detalhe_produto),
    path("pedidos/", view = views.listar_pedido_completo),
    path("pedidos/<int:id>", view = views.detalhe_pedido_completo),
    path("itempedido/", view = views.listar_item_pedido),
    path("itempedido/<int:id>", view = views.detalhe_item_pedido),
]
