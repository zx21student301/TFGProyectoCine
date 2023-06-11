from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .models import Pelicula

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .forms import *

# Create your views here.
class PeliculaListView(ListView):
    model = Pelicula
    
class PeliculaDetailView(DetailView):
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula = self.get_object()
        funciones = pelicula.funcion_set.all().order_by('fechaInicio')
        context['funciones'] = funciones
        return context

def administracion(request):
    template = loader.get_template("principal/administracion.html")
    return HttpResponse(template.render())

class PeliculaAdminListView(ListView):
    model = Pelicula
    template_name = 'principal/administracionPeliculas.html'
    context_object_name = 'peliculas'

class PeliculaCreatelView(CreateView):
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis', 'director', 'fechaLanzamiento', 'clasificacionEdad', 'disponible']
    success_url = reverse_lazy('listadoPelisAdmin')

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis', 'director', 'fechaLanzamiento', 'clasificacionEdad', 'disponible']
    template_name_suffix='_update_form'
    success_url = reverse_lazy('listadoPelisAdmin')

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('listadoPelisAdmin')

class SalaAdminListView(ListView):
    model = Sala
    template_name = 'principal/administracionSalas.html'
    context_object_name = 'salas'

class SalaCreatelView(CreateView):
    model = Sala
    fields = ['nombre', 'capacidadMaxima']
    success_url = reverse_lazy('listadoSalasAdmin')

class SalaUpdateView(UpdateView):
    model = Sala
    template_name_suffix='_update_form'
    fields = ['nombre', 'capacidadMaxima']
    success_url = reverse_lazy('listadoSalasAdmin')

class SalaDeleteView(DeleteView):
    model = Sala
    success_url = reverse_lazy('listadoSalasAdmin')

class FuncionAdminListView(ListView):
    model = Funcion
    template_name = 'principal/administracionFunciones.html'
    context_object_name = 'funciones'

class FuncionCreatelView(CreateView):
    model = Funcion
    fields = ['fecha', 'fechaInicio', 'fechaFin', 'pelicula', 'sala']
    success_url = reverse_lazy('listadoFuncionesAdmin')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Obtiene la función recién creada
        funcion = self.object

        # Crea las 40 butacas asignadas a la función
        for numero in range(1, 81):
            Butaca.objects.create(numero=numero, estado='Disponible', funcion=funcion)

        return response


class FuncionUpdateView(UpdateView):
    model = Funcion
    template_name_suffix='_update_form'
    fields = ['fecha', 'fechaInicio', 'fechaFin', 'pelicula', 'sala']
    success_url = reverse_lazy('listadoFuncionesAdmin')

class FuncionDeleteView(DeleteView):
    model = Funcion
    success_url = reverse_lazy('listadoFuncionesAdmin')


class ButacaAdminListView(ListView):
    model = Butaca
    template_name = 'principal/administracionButacas.html'
    context_object_name = 'butacas'
    ordering = ['funcion__id', 'numero']


class ButacaUpdateView(UpdateView):
    model = Butaca
    fields = ['estado', 'entrada']
    template_name_suffix='_update_form'
    success_url = reverse_lazy('listadoButacasAdmin')




def crear_butacas(sender, instance, created, **kwargs):
    if created:
        num_butacas = 40  # Número de butacas a crear
        for numero in range(1, num_butacas + 1):
            Butaca.objects.create(funcion=instance, numero=numero)

class FuncionDetailView(DetailView):
    model = Funcion

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['butacas'] = reversed(self.object.butaca_set.all())
            return context
