
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# to create views write a function that takes a request and return an HttpResponse
def index(request):
    return render(request, "hello/index.html")

def promit(request):
    return HttpResponse("hello return an HttpResponse.")

def akor(request):
    return HttpResponse("from RUMC .")

def greet(request,name):
    return HttpResponse(f"Hello {name.capitalize()}")
