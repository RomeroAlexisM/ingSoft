from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pedido, Tecnico, Usuario

# Create your views here.


def prueba(request):
    return HttpResponse("ESTO ES UNA PRUEBA")


def tecnico_pedidos(request):
    lista_todos_los_pedidos = Pedido.objects.all()
    return HttpResponse(json.dumps(lista_todos_los_pedidos))


