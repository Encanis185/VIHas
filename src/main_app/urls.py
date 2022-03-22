from django.urls import path
from . import views #desde nuestra carpeta actual, importa views

urlpatterns = [
    path('', views.home, name='main_page'),
    path('about/', views.about, name='about_page'),
]
