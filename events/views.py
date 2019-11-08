from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
    events = Event.objects
    return render(request, 'home/home.html', {'events':events})
