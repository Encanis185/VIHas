from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'main_app/home.html')


def about(request):
    return HttpResponse('<h1>About us</h>')