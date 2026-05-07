from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

class Comentario(models.Model):
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    texto = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.proyecto}"