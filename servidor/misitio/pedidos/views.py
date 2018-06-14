from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import detail_route

# Create your views here.

class UsuarioView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TecnicoView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()


class PedidoView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class PedidoMiUsuario(viewsets.ViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    lookup_field = 'autor'
    filter_backend = DjangoFilterBackend
    







