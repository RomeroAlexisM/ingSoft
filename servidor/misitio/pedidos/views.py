from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TecnicoView(viewsets.ModelViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()


class PedidoView(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()


class UsuarioABMView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class TecnicoABMView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()

class PedidoABMView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()