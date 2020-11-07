from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
import requests
import json
import string
from .apiFunctions import placesByStates
states = []
stateImages = []
with open("./project/static/statesImages.txt",'r') as fi:
    for i in fi.readlines():
        stateImages.append(i)
with open('./project/static/statesLocation.txt','r') as fi:
    j = 0
    for line in fi.readlines():
        words = line.split()
        name = words[0]
        li = []
        for i in range(1,len(words),2):
            li.append("{0} {1}".format(words[i],words[i+1]))
            dic = {'type':'POLYGON','vertices':li}
        #print([name,dic])
        url = stateImages[j].split()[-1]
        states.append([j,name,dic,url])
        j+=1
#print(states)
print(Person.objects.all())

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
    print(Person.objects.all())
    return render(request, 'home/home.html', {'range':range(10),'imageUrl':'https://tse1.mm.bing.net/th?id=OIP.p-qglTQvUYPA_bR0R9Eu3AHaEy&pid=Api','states':states})

def places(request):
    ind = request.path.rsplit('/',1)[1]
    place = states[int(ind)]
    places = placesByStates(place)
    #print("here -->",places)
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
    return render(request, 'home/landingpage.html', {name:"EXPLORE"})

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