from .models import Pedido, Usuario, Tecnico
from rest_framework import serializers


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id',
                  'email',
                  'password']


class TecnicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tecnico
        fields = ['id',
                  'email',
                  'password']


class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id',
                  'tipo_de_pedido',
                  'autor',
                  'tecnico_asignado',
                  'asunto',
                  'detalles',
                  'prioridad',
                  'sistema',
                  'fecha',
                  'archivo_adjunto'
                  ]
