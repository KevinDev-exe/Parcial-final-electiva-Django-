from django.urls import path
from .views import (
    ProyectoListView,
    ProyectoCreateView,
    ProyectoUpdateView,
    ProyectoDeleteView,
    ProyectoDetailView
)

app_name = 'proyectos'

urlpatterns = [
    path('', ProyectoListView.as_view(), name='list'),
    path('crear/', ProyectoCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', ProyectoUpdateView.as_view(), name='update'),
    path('eliminar/<int:pk>/', ProyectoDeleteView.as_view(), name='delete'),
    path('detalle/<int:pk>/', ProyectoDetailView.as_view(), name='detail'),
]