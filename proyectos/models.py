from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )
    titulo = models.CharField(max_length=200)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
