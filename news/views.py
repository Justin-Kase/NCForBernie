from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

def index(request):
    news = News.objects
    return render(request, 'home/home.html', {'news':news})
