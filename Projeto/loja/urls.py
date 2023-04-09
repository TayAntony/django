from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('clientes', views.ClienteViewSet)
router.register('cores', views.CorViewSet)

urlpatterns = [
    path('produtos', view=views.ProdutoList.as_view()),
    path('produtos/<int:pk>', view=views.ProdutoDetail.as_view()),
    path('categorias', view=views.Categoria.as_view()),
    path('categorias/<int:pk>/', view=views.CategoriaDetail.as_view())
]+ router.urls
