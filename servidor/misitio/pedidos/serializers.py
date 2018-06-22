from rest_framework import serializers
from rest_framework.serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions
from django.conf import settings
from django.utils.translation import gettext as _
import requests

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password')



class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('id',
                  'email',
                  'password')


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id',
                  'tipo_de_pedido',
                  'autor',
                  'tecnico_asignado',
                  'asunto',
                  'detalles',
                  'prioridad',
                  'sistema',
                  'fecha',
                  'archivo_adjunto')



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "Usuario desactivado"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Imposible loguear con los parametros dados"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Se necesita el username y password"
            raise exceptions.ValidationError(msg)
        return data
