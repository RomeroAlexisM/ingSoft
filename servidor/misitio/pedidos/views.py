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
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()


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


class LoginView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)









