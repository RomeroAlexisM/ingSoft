from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User #este es el usuario nativo de django
from rest_framework import viewsets, mixins
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TecnicoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()


class PedidoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class PedidoMiUsuarioSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all().order_by('-id').filter(autor = "3")

class Registrar(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UsuarioSerializer










