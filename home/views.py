from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
import requests
import json
import string
from .apiFunctions import placesByStates
fi = open("./project/static/statesLocation.txt",'r') 
states = []  
j = 0
for i in fi.readlines():
    states.append([j]+i.rsplit(maxsplit=3))
    j+=1
fi.close()
def home(request):
    #print(states)
    '''
    url = "https://rapidapi.p.rapidapi.com/images/search"
    querystring = {"q":"mahabalipuram","count":"1"}
    headers = {
        'x-rapidapi-key': "b7950242dbmsh896e4e949798a68p1a4a56jsn6aa4653dbb2b",
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    kk = json.loads(response.text)
    print(kk['value'][0]['thumbnailUrl'])
    '''
    return render(request, 'home/home.html', {'range':range(10),'imageUrl':'https://tse1.mm.bing.net/th?id=OIP.p-qglTQvUYPA_bR0R9Eu3AHaEy&pid=Api','states':states})

def places(request):
    ind = request.path.rsplit('/',1)[1]
    place = states[int(ind)]
    places = placesByStates(place)
    print("here -->",places)
    return render(request, 'home/placeslist.html', {'places':places})


def index(request):
    #print("hello")
    #print(Person.objects.all())
    try:
        k = request.POST['search']
        print(k)
    except:
        print("Not worked")
    #print(request.POST['exampleInputEmail1'])
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

def aboutus(request):
    return render(request, 'home/aboutus.html', {})

def blog(request):
    return render(request, 'blogs/blog.html', {'li':list(range(10))})