from django.shortcuts import render
from .models import Station,TrainRoutes,Train
from authentication import validate
from django.shortcuts import redirect
station = Station.objects.all().distinct('name')
# Create your views here.
routes = TrainRoutes.objects.all()
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
def index(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    try:
        k = request.POST
        print(k['destination'])
        des = k['destination']
        j = 0
        ans = []
        for i in routes:
            j+=1
            li = [i.source1,i.source2,i.source3,i.source4,i.source5,i.source6,i.source7,i.source8,i.source9,i.source10,i.source11,i.source12]
            ti = [i.time1,i.time2,i.time3,i.time4,i.time5,i.time6,i.time7,i.time8,i.time9,i.time10,i.time11,i.time12]
            if des in li:
                #print(j,'des found')
                jj = Train.objects.filter(no=i.no)
                #print(jj)
                ans.append([i,jj[0]])
        return render(request, 'train/trainsearch.html',{'station':station,'trains':ans,'days':days,'username':request.session['username']})

    except:
        print("from trains")
    return render(request, 'train/trainsearch.html',{'station':station,'username':request.session['username']})