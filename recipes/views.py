from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'recipes/home.html')

def about(request):
    return HttpResponse('My about')

def contact(request):
    return HttpResponse('My contact')