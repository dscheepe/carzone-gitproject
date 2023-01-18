from django.urls import path
from . import views # importeer views omdat we dit op R5 gebruiken

urlpatterns = [
    path('', views.home, name='home'),
    # '' is de homepage
    # views.home gaat in views zoeken naar de functie home
    # de naam voor deze op te roepen is home
    # Volgende stap maak in views.py de functie home
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
