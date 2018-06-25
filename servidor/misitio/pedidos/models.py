from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Usuario(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    es_tecnico = models.BooleanField(default = False)

# class Usuario(models.Model):
#     username = models.CharField(max_length=70, unique=True, null = True)
#     password = models.TextField(max_length=70, null=True)
#
#     def __str__(self):
#         return self.email
#
#
# class Tecnico(models.Model):
#     email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
#     password = models.TextField()
#
#     def __str__(self):
#         return self.email


class Pedido(models.Model):
    tipo_de_pedido = models.TextField()
    autor = models.ForeignKey(Usuario, related_name = 'autor', on_delete=models.CASCADE)
    tecnico_asignado = models.ForeignKey(Usuario, related_name = 'tecnico_asignado', on_delete=models.CASCADE)
    asunto = models.TextField()
    detalles = models.TextField()
    prioridad = models.TextField()
    sistema = models.TextField()
    fecha = models.TextField(null=True)
    archivo_adjunto = models.FileField(null=True)

    def __str__(self):
        return self.asunto
