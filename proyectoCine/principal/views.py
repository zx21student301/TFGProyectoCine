from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# Create your views here.
class PeliculaListView(ListView):
    model = Pelicula
    
class PeliculaDetailView(DetailView):
    model = Pelicula

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

class FuncionUpdateView(UpdateView):
    model = Funcion
    fields = ['fecha', 'fechaInicio', 'fechaFin', 'pelicula', 'sala']
    success_url = reverse_lazy('listadoFuncionesAdmin')

class FuncionDeleteView(DeleteView):
    model = Funcion
    success_url = reverse_lazy('listadoFuncionesAdmin')

