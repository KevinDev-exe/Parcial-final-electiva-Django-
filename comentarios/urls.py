from django.urls import path
from .views import crear_comentario

urlpatterns = [
    path('crear/<int:proyecto_id>/', crear_comentario, name='crear_comentario'),
]