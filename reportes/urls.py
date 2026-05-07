from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.lista_proyectos_reporte, name='lista'),
    path('csv/', views.exportar_proyectos_csv, name='exportar_csv'),
]
