from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")
