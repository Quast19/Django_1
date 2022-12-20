from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse

rooms = [
    {'id':1, 'name': 'lets learn python'},
    {'id':2, 'name': 'python and django'},
    {'id':3, 'name': 'backend is the key'}
]
# Create youBr views here.
def home(request):
    context = {'rooms':rooms}
    return render(request , 'home.html',context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'room.html', context)

def add(request):
    val1 =  int(request.POST['num1'])
    val2 =  int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html',{'result':res})