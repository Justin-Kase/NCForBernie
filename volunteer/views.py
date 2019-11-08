from django.shortcuts import render
from django.http import HttpResponse
from .models import Volunteer

def index(request):
    volunteer = Volunteer.objects
    title     = 'volunteer'
    return render(request, 'home/home.html', {'volunteer':volunteer, 'pageTitle':title})
