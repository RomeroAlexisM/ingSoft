from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def pedidos(request):
    return HttpResponse("ESTO ES LA PARTE DE PEDIDOS! FUNCIONÁ LA CONCHA DE TU HERMANA!.")
