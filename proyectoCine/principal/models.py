from django.db import models
from django.contrib.auth.models import Pelicula, Sala

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=700, verbose_name='Titulo')
    imagen = models.ImageField(verbose_name='foto ', upload_to='peliculas', verbose_name='imagen')
    genero = models.CharField(max_length=255, verbose_name='Genero')
    duracion = models.CharField(max_length=255, verbose_name='Duracion')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    director = models.CharField(max_length=255, verbose_name='Director')
    fechaLanzamiento = models.CharField(max_length=700, verbose_name='Fecha de lanzamiento')
    clasificacionEdad = models.CharField(max_length=255, verbose_name='Clasificacion edad')
    valoracion = models.FloatField(verbose_name='Valoracion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'pelicula'
        verbose_name_plural = "peliculas"
        ordering = ['-created']

    def __str__(self):
        return self.titulo


class Sala(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Capacidad maxima')
    capacidadMaxima = models.CharField(max_length=255, verbose_name='Capacidad maxima')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'sala'
        verbose_name_plural = "salas"
        ordering = ['-created']

    def __str__(self):
        return self.nombre


class Funcion(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    fechaInicio = models.DateTimeField(verbose_name='Hora inicio')
    fechaFin = models.DateTimeField(verbose_name='Hora fin')
    pelicula = models.ForeignKey(Pelicula, verbose_name='Pelicula', on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, verbose_name='Sala', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'funcion'
        verbose_name_plural = "funciones"
        ordering = ['-created']

    def __str__(self):
        return self.fechaInicio


class Usuario(models.Model):
    nombre = models.CharField(max_length=700)
    apellido = models.CharField(max_length=700)
    correoElectronico = models.CharField(max_length=700)
    contraseña = models.CharField(max_length=700)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'funcion'
        verbose_name_plural = "funciones"
        ordering = ['-created']

    def __str__(self):
        return self.fechaInicio


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

# CREATE TABLE Butacas (
#   Función INT,
#   Estado VARCHAR(50),
#   Entrada INT,
#   FOREIGN KEY (Función) REFERENCES Funciones(ID),
#   FOREIGN KEY (Entrada) REFERENCES Entradas(ID)
# );

# CREATE TABLE Usuarios (
#   nombre VARCHAR(700),
#   apellido VARCHAR(700),
#   correoElectronico VARCHAR(700),
#   contraseña VARCHAR(700)
# );
