from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación') 


# CREATE TABLE Películas (
#   titulo VARCHAR(255),
#   genero VARCHAR(255),
#   duracion INT,
#   sinopsis TEXT,
#   director VARCHAR(255),
#   fechaLanzamiento VARCHAR(255),
#   clasificacionEdad VARCHAR(50),
#   valoracion VARCHAR(50)
# );
