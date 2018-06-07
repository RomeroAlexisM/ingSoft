from django.shortcuts import render

# Create your views here.


from .serializers import *
# Create your views here.


class PedidosListaView():
    campo_de_busqueda = 'email'
    serializer_class = PedidoSerializer

    def get_queryset(self):
        return Pedido.objects.all()
