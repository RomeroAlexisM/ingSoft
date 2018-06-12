from django.urls import path, include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioView)
router.register('tecnicos', views.TecnicoView)
router.register('pedidos', views.PedidoView)


urlpatterns = [
    path('', include(router.urls))
]
