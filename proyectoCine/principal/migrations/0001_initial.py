# Generated by Django 4.2.1 on 2023-05-26 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=700, verbose_name='Titulo')),
                ('imagen', models.ImageField(upload_to='peliculas', verbose_name='Imagen')),
                ('genero', models.CharField(max_length=255, verbose_name='Genero')),
                ('duracion', models.CharField(max_length=255, verbose_name='Duracion')),
                ('sinopsis', models.TextField(verbose_name='Sinopsis')),
                ('director', models.CharField(max_length=255, verbose_name='Director')),
                ('fechaLanzamiento', models.CharField(max_length=700, verbose_name='Fecha de lanzamiento')),
                ('clasificacionEdad', models.CharField(max_length=255, verbose_name='Clasificacion edad')),
                ('valoracion', models.FloatField(verbose_name='Valoracion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'pelicula',
                'verbose_name_plural': 'peliculas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('descuento', models.FloatField(verbose_name='Descuento')),
                ('tipoDescuento', models.CharField(max_length=255, verbose_name='Tipo de descuento')),
                ('maxDescuento', models.FloatField(verbose_name='Maximo de descuento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'promocion',
                'verbose_name_plural': 'promociones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Capacidad maxima')),
                ('capacidadMaxima', models.CharField(max_length=255, verbose_name='Capacidad maxima')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'sala',
                'verbose_name_plural': 'salas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=700)),
                ('apellido', models.CharField(max_length=700)),
                ('correoElectronico', models.CharField(max_length=700)),
                ('contraseña', models.CharField(max_length=700)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UsuarioPromocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilizada', models.BooleanField(default=False, verbose_name='Utilizada')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('promocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.promocion', verbose_name='Promocion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuario y Promocion',
                'verbose_name_plural': 'Usuarios y Promociones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('fechaInicio', models.DateTimeField(verbose_name='Hora inicio')),
                ('fechaFin', models.DateTimeField(verbose_name='Hora fin')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.pelicula', verbose_name='Pelicula')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.sala', verbose_name='Sala')),
            ],
            options={
                'verbose_name': 'funcion',
                'verbose_name_plural': 'funciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'entrada',
                'verbose_name_plural': 'entradas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('puntuacion', models.IntegerField(verbose_name='Puntuacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.pelicula', verbose_name='Pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'comentario',
                'verbose_name_plural': 'comentarios',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Butaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(default='Disponible', max_length=255, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('entrada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.entrada', verbose_name='Entrada')),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.funcion', verbose_name='Funcion')),
            ],
            options={
                'verbose_name': 'butaca',
                'verbose_name_plural': 'butacas',
                'ordering': ['-created'],
            },
        ),
    ]
