from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'home.html',{'name':'Melwin'})

def add(request):
    return render(request, 'result.html',{'result':(int(request.POST['num1'])+int(request.POST['num2']))})