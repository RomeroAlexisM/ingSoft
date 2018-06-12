from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id',
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
