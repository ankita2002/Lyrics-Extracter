from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request): 
     return HttpResponse("<h1>Welcome to Ankita's Django App</h1>") 

