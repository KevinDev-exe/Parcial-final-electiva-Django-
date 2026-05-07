from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistroUsuarioForm


@login_required
def home(request):
    grupo = request.user.groups.first()
    return render(request, 'home.html', {'rol': grupo.name if grupo else 'Sin rol'})


def registro(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})
