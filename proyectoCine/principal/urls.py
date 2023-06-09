from django.urls import path
from .views import PeliculaListView,PeliculaDetailView
from . import views

urlpatterns = [
    path('', PeliculaListView.as_view(), name='listado'),
    path('pelicula/int:<pk>', PeliculaDetailView.as_view(), name="detalle"),
    path('register/', views.register_view, name='register_view'),
]