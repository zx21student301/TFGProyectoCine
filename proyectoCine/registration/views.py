from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm



def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirigir a la página de inicio después del registro
            return redirect('listado')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                    login(request, user)
                    if user.is_superuser:
                        return redirect("administracion")
                    return redirect("listado")
            else:
                messages.error(request,"Nombre de usuario o contraseña invalida.")
        else:
            messages.error(request,"Nombre de usuario o contraseña invalida.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})