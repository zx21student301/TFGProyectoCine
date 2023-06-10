from django import forms
from .models import *

class PeliculasForm(forms.ModelForm):
    class Meta:
        model=Pelicula
        fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis', 'director', 'fechaLanzamiento', 'clasificacionEdad', 'valoracion', 'disponible']
        
    


