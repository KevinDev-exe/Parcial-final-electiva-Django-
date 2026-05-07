from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone

from proyectos.models import Proyecto
from .models import Comentario
from .forms import ComentarioForm


@login_required
def crear_comentario(request, proyecto_id):

    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    # Validar si el proyecto ya está aprobado
    if proyecto.estado == 'aprobado':
        messages.error(
            request,
            'No se pueden agregar comentarios a un proyecto aprobado.'
        )
        return redirect('proyectos:detail', pk=proyecto.id)

    comentarios = Comentario.objects.filter(
        proyecto=proyecto
    ).order_by('-fecha')

    if request.method == 'POST':

        form = ComentarioForm(request.POST)

        if form.is_valid():

            comentario = form.save(commit=False)

            comentario.usuario = request.user
            comentario.proyecto = proyecto
            comentario.fecha = timezone.now()

            comentario.save()

            # Enviar correo al estudiante
            send_mail(
                subject='Nuevo comentario en tu proyecto',
                message=f'''
Hola {proyecto.estudiante.username},

Tu proyecto "{proyecto.titulo}" recibió un nuevo comentario.

Comentario:
{comentario.texto}

Fecha:
{comentario.fecha}
                ''',

                from_email='admin@gmail.com',
                recipient_list=[proyecto.estudiante.email],
                fail_silently=True,
            )

            messages.success(
                request,
                'Comentario agregado correctamente.'
            )

            return redirect(
                'crear_comentario',
                proyecto_id=proyecto.id
            )

    else:
        form = ComentarioForm()

    context = {
        'proyecto': proyecto,
        'comentarios': comentarios,
        'form': form,
    }

    return render(
        request,
        'comentarios/crear.html',
        context
    )