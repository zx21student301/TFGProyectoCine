from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .forms import *
from django.urls import reverse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json


# Create your views here.


class PeliculaListView(ListView):
    model = Pelicula


class PeliculaDetailView(DetailView):
    model = Pelicula

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula = self.get_object()
        funciones = pelicula.funcion_set.all().order_by('fechaInicio')
        context['funciones'] = funciones
        comentarios = pelicula.comentario_set.all().order_by('created')
        context['comentarios'] = comentarios
        users = User.objects.all()  # Obtener todos los usuarios
        context['users'] = users
        return context

@login_required
def administracion(request):
    template = loader.get_template("principal/administracion.html")
    return HttpResponse(template.render())

        

@method_decorator(login_required, name='dispatch')
class PeliculaAdminListView(ListView):
    model = Pelicula
    template_name = 'principal/administracionPeliculas.html'
    context_object_name = 'peliculas'

@method_decorator(login_required, name='dispatch')
class PeliculaCreatelView(CreateView):
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis',
              'director', 'fechaLanzamiento', 'clasificacionEdad', 'disponible']
    success_url = reverse_lazy('listadoPelisAdmin')

@method_decorator(login_required, name='dispatch')
class PeliculaUpdateView(UpdateView):
    model = Pelicula
    fields = ['titulo', 'imagen', 'genero', 'duracion', 'sinopsis',
              'director', 'fechaLanzamiento', 'clasificacionEdad', 'disponible']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listadoPelisAdmin')

@method_decorator(login_required, name='dispatch')
class PeliculaDeleteView(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('listadoPelisAdmin')

@method_decorator(login_required, name='dispatch')
class SalaAdminListView(ListView):
    model = Sala
    template_name = 'principal/administracionSalas.html'
    context_object_name = 'salas'

@method_decorator(login_required, name='dispatch')
class SalaCreatelView(CreateView):
    model = Sala
    fields = ['nombre', 'capacidadMaxima']
    success_url = reverse_lazy('listadoSalasAdmin')

@method_decorator(login_required, name='dispatch')
class SalaUpdateView(UpdateView):
    model = Sala
    template_name_suffix = '_update_form'
    fields = ['nombre', 'capacidadMaxima']
    success_url = reverse_lazy('listadoSalasAdmin')

@method_decorator(login_required, name='dispatch')
class SalaDeleteView(DeleteView):
    model = Sala
    success_url = reverse_lazy('listadoSalasAdmin')

@method_decorator(login_required, name='dispatch')
class FuncionAdminListView(ListView):
    model = Funcion
    template_name = 'principal/administracionFunciones.html'
    context_object_name = 'funciones'

@method_decorator(login_required, name='dispatch')
class FuncionCreatelView(CreateView):
    model = Funcion
    fields = ['fecha', 'fechaInicio', 'fechaFin', 'pelicula', 'sala']
    success_url = reverse_lazy('listadoFuncionesAdmin')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Obtiene la función recién creada
        funcion = self.object

        # Crea las 40 butacas asignadas a la función
        for numero in range(1, 81):
            Butaca.objects.create(
                numero=numero, estado='Disponible', funcion=funcion)

        return response

@method_decorator(login_required, name='dispatch')
class FuncionUpdateView(UpdateView):
    model = Funcion
    template_name_suffix = '_update_form'
    fields = ['fecha', 'fechaInicio', 'fechaFin', 'pelicula', 'sala']
    success_url = reverse_lazy('listadoFuncionesAdmin')

@method_decorator(login_required, name='dispatch')
class FuncionDeleteView(DeleteView):
    model = Funcion
    success_url = reverse_lazy('listadoFuncionesAdmin')

@method_decorator(login_required, name='dispatch')
class ButacaAdminListView(ListView):
    model = Butaca
    template_name = 'principal/administracionButacas.html'
    context_object_name = 'butacas'
    ordering = ['funcion__id', 'numero']

@method_decorator(login_required, name='dispatch')
class ButacaUpdateView(UpdateView):
    model = Butaca
    fields = ['estado', 'entrada']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listadoButacasAdmin')


def crear_butacas(sender, instance, created, **kwargs):
    if created:
        num_butacas = 40  # Número de butacas a crear
        for numero in range(1, num_butacas + 1):
            Butaca.objects.create(funcion=instance, numero=numero)


@method_decorator(login_required, name='dispatch')
class FuncionDetailView(DetailView):
    model = Funcion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['butacas'] = reversed(self.object.butaca_set.all())
        return context


@csrf_exempt
def crear_entrada(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        precio = data.get('precio')

        if precio is not None:
            # Crea la entrada en la base de datos
            entrada = Entrada(usuario=request.user, precio=precio)
            entrada.save()

            return JsonResponse({'message': 'Entrada creada exitosamente', 'id': entrada.id, 'user_id': request.user.id})
        else:
            return JsonResponse({'message': 'Datos incorrectos'})
    else:
        return JsonResponse({'message': 'Método no permitido'})


@login_required
def crearComentario(request):
    id_p = request.GET['pelicula_id']
    pelicula = Pelicula.objects.get(id=id_p)

    id_u = request.user
    c = request.GET['comentario']
    p = request.GET['puntuacion']

    coment = Comentario(usuario = id_u, pelicula = pelicula, comentario = c, puntuacion = p)
    coment.save()

    return HttpResponseRedirect(reverse('detalle', args=[id_p]))

def borrarComentario(request,identificador,id_p):
    Comentario.objects.filter(id=identificador).delete()

    return HttpResponseRedirect(reverse('detalle', args=[id_p]))

def updateComentario(request,id_p):
    idp = request.GET['comentario_id']

    ob = Comentario.objects.get(id=idp)

    nc = request.GET['comentario_nuevo']
    np = request.GET['puntuacion_nueva']

    ob.comentario = nc
    ob.puntuacion = np
    ob.save()

    return HttpResponseRedirect(reverse('detalle', args=[id_p]))
    
@csrf_exempt
def modificar_butaca(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entrada_id = data.get('entradaId')
        butaca_id = data.get('butacaId') # Obtiene el ID de la butaca desde la solicitud

        # Realiza la modificación de la butaca en la base de datos
        try:
            butaca = Butaca.objects.get(id=butaca_id) # Utiliza el ID de la butaca para obtener el objeto de la base de datos
            # Modifica los campos de la butaca según tus necesidades
            entrada = Entrada.objects.get(id=entrada_id)
            butaca.entrada = entrada
            butaca.estado = 'ocupado'
            butaca.save()

            # Devuelve una respuesta JSON indicando que la butaca se modificó correctamente
            response_data = {'message': 'Butaca modificada exitosamente'}
            return JsonResponse(response_data)
        except Butaca.DoesNotExist:
            # Si la butaca no existe, devuelve un mensaje de error
            response_data = {'error': 'La butaca no existe'}
            return JsonResponse(response_data, status=400)

@method_decorator(login_required, name='dispatch')
class UsuarioDetailView(DetailView):
    model = User



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        entradas = Entrada.objects.filter(usuario=user).order_by('-created')
        butacas_por_entrada = []
        funcion_por_entrada = []
        sala_por_entrada = []
        pelicula_por_entrada = []
        for entrada in entradas:
            butacas = Butaca.objects.filter(entrada=entrada).order_by('-created')
            butacas_por_entrada.append(butacas)
            if butacas.exists():
                funcion = butacas.first().funcion
                sala = funcion.sala
                pelicula = funcion.pelicula
                sala_por_entrada.append(sala)
                funcion_por_entrada.append(funcion)
                pelicula_por_entrada.append(pelicula)
        
        context['entradas'] = entradas
        context['butacas_por_entrada'] = butacas_por_entrada
        context['funcion_por_entrada'] = funcion_por_entrada
        context['pelicula_por_entrada'] = pelicula_por_entrada
        context['sala_por_entrada'] = sala_por_entrada
        return context

@method_decorator(login_required, name='dispatch')
class ComentarioAdminListView(ListView):
    model = Comentario
    template_name = 'principal/administracionComentario.html'
    context_object_name = 'comentarios'

@method_decorator(login_required, name='dispatch')
class ComentarioAdminDeleteView(DeleteView):
    model = Comentario
    success_url = reverse_lazy('listadoComentariosAdmin')



@method_decorator(login_required, name='dispatch')
class EntradaAdminListView(ListView):
    model = Entrada
    template_name = 'principal/administracionEntradas.html'
    context_object_name = 'entradas'