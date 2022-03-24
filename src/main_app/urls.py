from django.urls import path
from . import views #desde nuestra carpeta actual, importa views

urlpatterns = [
    path('', views.home, name='main_page'),
    path('about/', views.about, name='about_page'),
    path('donacion/',views.donation,name='donation_page'),
    path('prueba/',views.prueba,name='prueba_page'),
    path('preguntas/',views.preguntas,name='preguntas_page'),
    path('contacto/',views.contacto,name='contacto_page'),
]
