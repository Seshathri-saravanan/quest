from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
import requests
import json
import string
from places.models import TouristPlaces
from django.db.models import Q
from authentication import validate
from django.shortcuts import redirect
states = []
stateImages = []
categories = [['Historical places','historical'],['Beaches','beaches'],['National parks','parks'],['Hill stations','hills'],['temples','temples'],['cities','cities']]
with open("./project/static/statesImages.txt",'r') as fi:
    j = 0
    for i in fi.readlines():
        li = [j]+ list(i.rsplit(maxsplit=1))
        stateImages.append(li)
        j+=1
#print(stateImages)
#saveInDatabase('')

def index(request):
    print("from home ind")
    if validate.alreadyLoggedIN(request):
        return redirect('/home')
    return render(request, 'home/landingpage.html',{})
'''
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
for i in states[24:]:
    placesByStates(i)
'''
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
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'home/home.html', {'range':range(10),'imageUrl':'https://tse1.mm.bing.net/th?id=OIP.p-qglTQvUYPA_bR0R9Eu3AHaEy&pid=Api','states':stateImages,'categories':categories,'username':request.session['username']})

def places(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    ind = request.path.rsplit('/',1)
    if(ind[0]=="/states"):
        place = stateImages[int(ind[1])][1]
        places = TouristPlaces.objects.all().filter(Q(state=place) & ~Q(category=7315023) & ~Q(category=7314003) )
    elif ind[0]=="/categories":
        if ind[1]=='beaches':
            places = TouristPlaces.objects.all().filter(category=9357)
        elif ind[1]=='historical':
            places = TouristPlaces.objects.all().filter(category=7376003)
        elif ind[1]=='temples':
            places = TouristPlaces.objects.all().filter(category=7339005)
        elif ind[1]=='hills':
            places = TouristPlaces.objects.all().filter(Q(category=7337) | Q(category=7376004))
        elif ind[1]=='parks':
            places = TouristPlaces.objects.all().filter(name__contains="Park")

    #print(places)
    #places = placesByStates(place)
    #print("here -->",places)
    return render(request, 'home/placeslist.html', {'places':places})

def historical(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/historical.html', {'placename':"HISTORICAL PLACES"})

def cities(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/cities.html', {'placename':"MAJOR CITIES"})

def parks(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/parks.html', {'placename':"NATIONAL PARKS"})

def beaches(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/beaches.html', {'placename':"BEACHES"})

def temples(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/temples.html', {'placename':"TEMPLES"})

def hills(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/hills.html', {'placename':"HILL STATIONS"})

def aboutus(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'home/aboutus.html', {})

def blog(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'blogs/blog.html', {'li':list(range(10))})