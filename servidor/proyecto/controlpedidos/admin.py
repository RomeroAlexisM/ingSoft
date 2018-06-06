from django.contrib import admin

# Register your models here.
from .models import Tecnico, Pedido, Usuario

admin.site.register(Pedido)
admin.site.register(Usuario)
admin.site.register(Tecnico)
