from django.shortcuts import render
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):       
      return render(request, "flights/index.html", {
         "flights": Flight.objects.all(),  
         
       })

def flightinfo(request,flight_id):  
      flight=Flight.objects.get(id=flight_id)
      print("flight id is:" , flight_id)  # This should output the correct ID  
      return render(request, "flights/flightinfo.html", {
         "flightinfo": flight,
         "passengers_all": Passenger.objects.all().order_by('first'),
         "passengers_in_flight": flight.passengers.all().order_by('first'),
         "flight_id": flight_id
       })
      
def add_passengers_to_flight(request, flight_id):
    flight=Flight.objects.get(id=flight_id)
    print("ftttfffflight id is:" , flight_id, flight.id, flight)  # This should output the correct ID  
    if request.method == 'POST':
      selected_passenger_ids = request.POST.getlist('add_passengers')
      add_passengers = Passenger.objects.filter(id__in=selected_passenger_ids)
      for passenger in add_passengers:
        flight.passengers.add(passenger)    
        print("flight id is:" , flight_id)  # This should output the correct ID  
      return HttpResponseRedirect(reverse("add_passengers_to_flight", args=[flight_id]))
    else:
      return render(request, "flights/flightinfo.html", {
         "flightinfo": flight,
         "passengers_all": Passenger.objects.all().order_by('first'),
         "passengers_in_flight": flight.passengers.all().order_by('first'),
         "flight_id": flight_id
       })
      

