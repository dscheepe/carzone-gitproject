from django.shortcuts import render
from .models import Team

# Create your views here.

# Maak een functie home en geef de request mee door als parameter
def home(request):
    teams = Team.objects.all() # Haalt alle data op van (R2) Class Team en steekt deze in teams
    data = {
        'team_data': teams,    # Haalt de data uit teams (R8) deze wordt doorgegeven naar de data variabelen naar html waar we met team_data de waarde kunnen uitlezen
    }
    return render(request, 'pages/home.html', data )

def about(request):
    teams = Team.objects.all()
    data = {
        'team_data': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request,'pages/services.html' )

def contact(request):
    return render(request, 'pages/contact.html')

