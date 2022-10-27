from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_produto/', views.criar_produto, name='adicionar_produto'),
    path('excluir_produto/<int:id>',views.excluir_produto , name='excluir_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
]