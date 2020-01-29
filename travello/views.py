from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    dest1 = Destination()
    dest1.name = 'Kerala'
    dest1.desc = 'Gods Own Countery !'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Kerala1'
    dest2.desc = 'Gods Own Countery !'
    dest2.price = 700
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Kerala2'
    dest3.desc = 'Gods Own Countery !'
    dest3.price = 700
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1,dest2,dest3]
    return render(request, 'index.html',{'dests':dests})