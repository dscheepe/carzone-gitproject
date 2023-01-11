from django.shortcuts import render

# Create your views here.

# Maak een functie home en geef de request mee door als parameter
def home(request):
    return render(request, 'pages/home.html' )
    # return en render de request die meegegeven is aan de functie
    # gaat de template in pages/home.html renderen
    # Maak eerst een template aan
    # Creeer de folder pages en file home.html
