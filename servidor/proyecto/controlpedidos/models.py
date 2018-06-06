from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    password = models.TextField()


class Tecnico(models.Model):
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    password = models.TextField()


class Pedido(models.Model):
    tipo_de_pedido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tecnico_asignado = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    asunto = models.TextField()
    detalles = models.TextField()
    prioridad = models.TextField()
    sistema = models.TextField()
    fecha = models.DateTimeField('Fecha Publicada')
    archivo_adjunto = models.FileField()


