from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('tecnicos', views.TecnicoViewSet)
router.register('pedidos', views.PedidoViewSet)
router.register('mispedidos', views.PedidoMiUsuarioSet)
router.register('registrar', views.Registrar, base_name = 'registro')


urlpatterns = [
    path('', include(router.urls))
]
