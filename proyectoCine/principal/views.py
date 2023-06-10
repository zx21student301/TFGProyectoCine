from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Pelicula
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
    print("Asd")
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis', 'director', 'fechaLanzamiento', 'clasificacionEdad', 'disponible']



