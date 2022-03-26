from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    context = {
        'title':'VIHas de VIDA'
    }
    return render(request, 'main_app/index.html', context)


def acerca(request):
    context = {
        'title':'Acerca de nosotros'
    }
    return render(request, 'main_app/acerca.html', context)

def donacion(request):
    context = {
        'title':'Tus donaciones salvan vidas'
    }
    return render(request, 'main_app/donacion.html', context)

def prueba(request):
    context = {
        'title':'Hazte la prueba'
    }
    return render(request, 'main_app/prueba.html', context)

def preguntas(request):
    context = {
        'title':'Preguntas frecuentes'
    }
    return render(request, 'main_app/preguntas.html', context)

def contacto(request):
    context = {
        'title':'Contacto'
    }
    return render(request, 'main_app/contacto.html', context)
