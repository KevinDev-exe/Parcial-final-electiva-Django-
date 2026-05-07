from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'documento']

class ProyectoEvaluarForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['estado', 'calificacion']