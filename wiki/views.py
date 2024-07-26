from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"wiki/homepage.html")

def landing(request):
    return HttpResponse("page-2!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

# def homepage(request):
#     return render(request, "wiki/homepage.html") 
