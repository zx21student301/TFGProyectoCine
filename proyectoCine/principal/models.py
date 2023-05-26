from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    imagen = models.ImageField(verbose_name='foto ',upload_to='peliculas',)
    genero = models.CharField(max_length=255)
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    director = models.CharField(max_length=255)
    fechaLanzamiento = models.CharField(max_length=255)
    clasificacionEdad = models.CharField(max_length=50)
    valoracion = models.FloatField()
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')

    class Meta:
        verbose_name='pelicula'
        verbose_name_plural="peliculas"
        ordering=['-created']
    
    def __str__(self):
        return self.titulo

# CREATE TABLE Películas (
#   titulo VARCHAR(255),
#   genero VARCHAR(255),
#   duracion INT,
#   sinopsis TEXT,
#   director VARCHAR(255),
#   fechaLanzamiento VARCHAR(255),
#   clasificacionEdad VARCHAR(50),
#   valoracion float
# );
