from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
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
