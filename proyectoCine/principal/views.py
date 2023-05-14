from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    template = loader.get_template("principal/base.html")
    return HttpResponse(template.render())