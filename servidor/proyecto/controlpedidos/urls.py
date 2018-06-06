from django.urls import path

from . import views

urlpatterns = [
    path('prueba', views.prueba, name='index'),
    path('tecnico/pedidos', views.tecnico_pedidos, name='lista_pedidos_tecnico'),
]