from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proyecto
from .forms import ProyectoForm, ProyectoEvaluarForm
from django.utils import timezone


# LISTAR PROYECTOS
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyectos/list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        user = self.request.user

        # estudiante solo ve los suyos
        if user.groups.filter(name='Estudiante').exists():
            return Proyecto.objects.filter(estudiante=user)

        # docente ve todos
        return Proyecto.objects.all()


# CREAR PROYECTO
class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/form.html'
    success_url = reverse_lazy('proyectos:list')

    def form_valid(self, form):
        form.instance.estudiante = self.request.user
        return super().form_valid(form)


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    template_name = 'proyectos/form.html'
    success_url = reverse_lazy('proyectos:list')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Docente').exists():
            return ProyectoEvaluarForm
        return ProyectoForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # estudiante solo puede editar si es su proyecto
        if request.user.groups.filter(name='Estudiante').exists() and obj.estudiante != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.groups.filter(name='Docente').exists():
            form.instance.fecha_revision = timezone.now()
        return super().form_valid(form)


# ELIMINAR PROYECTO
class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'proyectos/delete.html'
    success_url = reverse_lazy('proyectos:list')


# DETALLE PROYECTO
class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = 'proyectos/detail.html'
    context_object_name = 'proyecto'