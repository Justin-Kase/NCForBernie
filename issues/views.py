from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue


def index(request):
    issues = Issue.objects
    return render(request, 'issues/issues.html', {'issues':issues})
