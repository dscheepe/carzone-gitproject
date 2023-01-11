from django.urls import path
from . import views # importeer views omdat we dit op R5 gebruiken

urlpatterns = [
    path('', views.home, name='home'),
    # '' is de homepage
    # views.home gaat in views zoeken naar de functie home
    # de naam voor deze opo te roepen is home
    # Volgende stap maak in views.py de functie home
]
