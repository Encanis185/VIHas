from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'main_app/index.html')


def about(request):
    return HttpResponse('<h1>About us</h>')

def donation(request):
    return HttpResponse('<h1>Haz una donación</h>')

def prueba(request):
    return HttpResponse('<h1>Hazte la prueba</h>')

def preguntas(request):
    return HttpResponse('<h1>Preguntas Frecuentes<h>')

def contacto(request):
    return HttpResponse('<h1>Contacto<h>')
