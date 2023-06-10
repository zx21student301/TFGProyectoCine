from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=700, verbose_name='Titulo')
    imagen = models.ImageField( upload_to='peliculas', verbose_name='Imagen')
    genero = models.CharField(max_length=255, verbose_name='Genero')
    duracion = models.CharField(max_length=255, verbose_name='Duracion')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    director = models.CharField(max_length=255, verbose_name='Director')
    fechaLanzamiento = models.CharField(max_length=700, verbose_name='Fecha de lanzamiento')
    clasificacionEdad = models.CharField(max_length=255, verbose_name='Clasificacion edad')
    valoracion = models.FloatField(verbose_name='Valoracion', null=True)
    disponible = models.BooleanField(default=True, verbose_name='Disponible')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'pelicula'
        verbose_name_plural = "peliculas"
        ordering = ['-created']

    def __str__(self):
        return self.titulo


class Sala(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
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


# class Usuario(models.Model):
#     nombre = models.CharField(max_length=700)
#     apellido = models.CharField(max_length=700)
#     correoElectronico = models.CharField(max_length=700)
#     contraseña = models.CharField(max_length=700)
#     administrador = models.BooleanField(default=False, verbose_name='Administrador')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

#     class Meta:
#         verbose_name = 'usuario'
#         verbose_name_plural = "usuarios"
#         ordering = ['-created']

#     def __str__(self):
#         return self.nombre
    
class Entrada(models.Model):
    precio = models.FloatField(verbose_name='Precio')
    usuario = models.ForeignKey(User, verbose_name='Usuario' , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = "entradas"
        ordering = ['-created']

class Butaca(models.Model):
    estado = models.CharField(max_length=255, default='Disponible', verbose_name='Estado')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, verbose_name='Funcion')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, null=True, verbose_name='Entrada')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'butaca'
        verbose_name_plural = "butacas"
        ordering = ['-created']

class Comentario(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario' , on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, verbose_name='Pelicula' , on_delete=models.CASCADE)
    comentario = models.TextField(verbose_name='Comentario')
    puntuacion = models.IntegerField(verbose_name='Puntuacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = "comentarios"
        ordering = ['-created']

class Promocion(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    descuento = models.FloatField(verbose_name='Descuento')
    tipoDescuento = models.CharField(max_length=255, verbose_name='Tipo de descuento')
    maxDescuento = models.FloatField(verbose_name='Maximo de descuento')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'promocion'
        verbose_name_plural = "promociones"
        ordering = ['-created']

class UsuarioPromocion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, verbose_name='Promocion')
    utilizada = models.BooleanField(default=False, verbose_name='Utilizada')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Usuario y Promocion'
        verbose_name_plural = "Usuarios y Promociones"
        ordering = ['-created']

