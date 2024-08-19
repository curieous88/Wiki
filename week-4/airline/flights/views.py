from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):       
      return render(request, "flights/index.html", {
         "flights": Flight.objects.all(),  
         
       })

def flightinfo(request,flight_id):  
      flight=Flight.objects.get(id=flight_id)
      return render(request, "flights/flightinfo.html", {
         "flightinfo": flight,
         "passengers_all": Passenger.objects.all(),
         "passengers_in_flight": flight.passengers.all()
       })
      
# def book(request, flight_id):
#   if request.method == "POST":
#     flight=Flight.objects.get(flight_id)
#     return HttpResponseRedirect
    
      


