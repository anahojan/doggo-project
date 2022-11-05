from django.shortcuts import render
from .models import Room

""" rooms = [
    {'id': 1, 'name': 'Lets find a perfect dog for you!'},
    {'id': 2, 'name': 'Lets meet up!'},
    {'id': 3, 'name': 'Find a dogwalker'},
    {'id': 4, 'name': 'Find a breeder!'},
    {'id': 5, 'name': 'Doggo destress!'},
] """

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)