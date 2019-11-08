from django.shortcuts import render
from django.http import HttpResponse
from issues.models import Issue

def index(request):
    issues = Issue.objects
    return render(request, 'home/home.html', {'issues':issues})
