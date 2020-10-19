from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home/landingpage.html', {})

def historical(request):
    return render(request, 'places/historical.html', {'placename':"HISTORICAL PLACES"})

def cities(request):
    return render(request, 'places/cities.html', {'placename':"MAJOR CITIES"})

def parks(request):
    return render(request, 'places/parks.html', {'placename':"NATIONAL PARKS"})

def beaches(request):
    return render(request, 'places/beaches.html', {'placename':"BEACHES"})

def temples(request):
    return render(request, 'places/temples.html', {'placename':"TEMPLES"})

def hills(request):
    return render(request, 'places/hills.html', {'placename':"HILL STATIONS"})

