from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    template = loader.get_template("principal/base.html")
    return HttpResponse(template.render())

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal/base.html')
            else:
                error_message = 'Error al registrar el usuario. Inténtalo de nuevo.'
                return render(request, 'principal/base.html', {'error_message': error_message})
    else:
        form = UserCreationForm()
    return render(request, 'principal/base.html', {'form': form})

