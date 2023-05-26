from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirigir a la página de inicio después del registro
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registro.html', {'form': form})
