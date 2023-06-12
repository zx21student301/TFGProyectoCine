from django.urls import path

from .views import *

from .views import PeliculaListView,PeliculaDetailView

from . import views

urlpatterns = [
    path('', PeliculaListView.as_view(), name='listado'),
    path('pelicula/int:<pk>', PeliculaDetailView.as_view(), name="detalle"),
    path('', views.crear_comentario, name="crear_comentario"),
    path('administracion/',  views.administracion ,name='administracion'),
    path('administracion/peliculas',  PeliculaAdminListView.as_view() ,name='listadoPelisAdmin'),
    path('administracion/peliculas/crear',  PeliculaCreatelView.as_view() ,name='crearPelisAdmin'),
    path('modificarPelicula/<int:pk>', PeliculaUpdateView.as_view(), name="modificarPelicula"),
    path('borrarPelicula/<int:pk>', PeliculaDeleteView.as_view(), name="borrarPelicula"),
    path('administracion/salas',  SalaAdminListView.as_view() ,name='listadoSalasAdmin'),
    path('administracion/salas/crear',  SalaCreatelView.as_view() ,name='crearSalasAdmin'),
    path('modificarSala/<int:pk>', SalaUpdateView.as_view(), name="modificarSala"),
    path('borrarSala/<int:pk>', SalaDeleteView.as_view(), name="borrarSala"),
    path('administracion/funciones',  FuncionAdminListView.as_view() ,name='listadoFuncionesAdmin'),
    path('administracion/funciones/crear',  FuncionCreatelView.as_view() ,name='crearFuncionesAdmin'),
    path('modificarFuncion/<int:pk>', FuncionUpdateView.as_view(), name="modificarFuncion"),
    path('borrarFuncion/<int:pk>', FuncionDeleteView.as_view(), name="borrarFuncion"),
    path('administracion/Butacas',  ButacaAdminListView.as_view() ,name='listadoButacasAdmin'),
    path('modificarButaca/<int:pk>', ButacaUpdateView.as_view(), name="modificarButaca"),
    path('funcion/int:<pk>', FuncionDetailView.as_view(), name="detalleFuncion"),
    path('funcion/crearEntrada/', crear_entrada, name='crearEntrada'),
]