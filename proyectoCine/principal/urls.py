from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PeliculaListView.as_view(), name='listado'),
    path('pelicula/int:<pk>', PeliculaDetailView.as_view(), name="detalle"),
    path('administracion/',  views.administracion ,name='administracion'),
    path('administracion/peliculas',  PeliculaAdminListView.as_view() ,name='listadoPelisAdmin'),
    path('administracion/peliculas/crear',  PeliculaCreatelView.as_view() ,name='crearPelisAdmin'),
]