from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

<<<<<<< Updated upstream
=======
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Pelicula
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *
from django.urls import reverse_lazy

>>>>>>> Stashed changes
# Create your views here.
def index(request):
    template = loader.get_template("principal/base.html")
    return HttpResponse(template.render())

def administracion(request):
    template = loader.get_template("principal/administracion.html")
    return HttpResponse(template.render())

class PeliculaAdminListView(ListView):
    model = Pelicula
    template_name = 'principal/administracionPeliculas.html'
    context_object_name = 'peliculas'

class PeliculaCreatelView(CreateView):
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis', 'director', 'fechaLanzamiento', 'clasificacionEdad', 'valoracion', 'disponible']




