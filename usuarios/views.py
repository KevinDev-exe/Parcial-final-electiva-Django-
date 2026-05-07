from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import RegistroForm
from .models import Perfil


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            rol = form.cleaned_data['rol']

            # Crear o asignar grupo
            grupo, _ = Group.objects.get_or_create(name=rol)
            user.groups.add(grupo)

            # Crear perfil
            Perfil.objects.create(usuario=user, rol=rol)

            login(request, user)
            messages.success(request, f'Cuenta creada como {rol}.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def home(request):
    return render(request, 'home.html')