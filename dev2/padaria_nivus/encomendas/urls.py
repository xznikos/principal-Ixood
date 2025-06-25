from django.contrib import admin
from django.urls import path
from . import views

app_name = "encomendas"

urlpatterns = [
    path('', views.encomendas_home, name="home"),
    path('adicionar/', views.adicionar_home, name="adicionar"),
    path('remover/<int:id>',views.remover_home, name="remover"),
    path('editar/<int:id>', views.editar_encomenda, name="editar"),
    path('teste/', views.teste_home, name="teste")
]