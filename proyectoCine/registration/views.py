from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


from django.contrib.auth import login, authenticate


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirigir a la página de inicio después del registro
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # El usuario se autenticó correctamente
            login(request, user)
            # Redirigir a la página deseada después del inicio de sesión
            return redirect('index')
        else:
            # El usuario no se autenticó correctamente
            error_message = "Correo electrónico o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')