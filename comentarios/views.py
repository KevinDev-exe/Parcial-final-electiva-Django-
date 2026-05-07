from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail

from proyectos.models import Proyecto
from .models import Comentario
from .forms import ComentarioForm


def crear_comentario(request, proyecto_id):

    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if proyecto.estado == 'aprobado':
        messages.error(request, 'No se pueden agregar comentarios.')
        return redirect('detalle_proyecto', proyecto_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.proyecto = proyecto
            comentario.save()

            send_mail(
                'Nuevo comentario',
                'Tu proyecto recibió un comentario.',
                'admin@gmail.com',
                [proyecto.estudiante.email],
                fail_silently=False,
            )

            return redirect('detalle_proyecto', proyecto_id)

    else:
        form = ComentarioForm()

    return render(request, 'comentarios/crear.html', {'form': form})