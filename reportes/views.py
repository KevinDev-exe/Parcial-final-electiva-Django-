from django.shortcuts import render
from django.http import HttpResponse
from proyectos.models import Proyecto
import csv

def lista_proyectos_reporte(request):
    proyectos = Proyecto.objects.all()
    
    estado_filtro = request.GET.get('estado', '')
    estudiante_filtro = request.GET.get('estudiante', '')
    
    if estado_filtro:
        proyectos = proyectos.filter(estado=estado_filtro)
    if estudiante_filtro:
        proyectos = proyectos.filter(estudiante__username__icontains=estudiante_filtro)
        
    context = {
        'proyectos': proyectos,
        'estado_filtro': estado_filtro,
        'estudiante_filtro': estudiante_filtro,
        'estados': Proyecto.ESTADOS,
    }
    return render(request, 'reportes/lista_proyectos.html', context)

def exportar_proyectos_csv(request):
    proyectos = Proyecto.objects.all()
    
    estado_filtro = request.GET.get('estado', '')
    estudiante_filtro = request.GET.get('estudiante', '')
    
    if estado_filtro:
        proyectos = proyectos.filter(estado=estado_filtro)
    if estudiante_filtro:
        proyectos = proyectos.filter(estudiante__username__icontains=estudiante_filtro)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_proyectos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Título', 'Estudiante', 'Estado', 'Calificación', 'Fecha de Envío'])

    for p in proyectos:
        writer.writerow([
            p.titulo,
            p.estudiante.username if p.estudiante else '',
            p.get_estado_display(),
            p.calificacion if p.calificacion is not None else 'N/A',
            p.fecha_envio.strftime("%Y-%m-%d %H:%M") if p.fecha_envio else ''
        ])

    return response
