from django.shortcuts import render, get_object_or_404
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
      # print("flight id is:" , flight_id)  # This should output the correct ID  
      return render(request, "flights/flightinfo.html", {
         "flightinfo": flight,
         "passengers_all": Passenger.objects.all().order_by('first'),
         "passengers_in_flight": flight.passengers.all().order_by('first'),
         "flight_id": flight_id
       })
      
def add_passengers_to_flight(request, flight_id):
    flight=Flight.objects.get(id=flight_id)
    print("test flight id is:" , flight_id, flight.id, flight)  # This should output the correct ID  
    if request.method == "POST":
      selected_passengers = request.POST.getlist("add_passengers")  # Get a list of selected passenger IDs
      print("Selected passenger IDs:", selected_passengers)  # Debug output
      for selected_passenger_id in selected_passengers:
          selected_passenger = get_object_or_404(Passenger, pk=int(selected_passenger_id))
          print("Test passenger ID is:", selected_passenger_id)
          # Add the passenger to the flight or perform any other necess
          flight.passengers.add(selected_passenger)    
      flight.save()
      return HttpResponseRedirect(reverse("add_passengers_to_flight", args=[flight.id]))
    else:
      return render(request, "flights/flightinfo.html", {
         "flightinfo": flight,
         "passengers_all": Passenger.objects.all().order_by('first'),
         "passengers_in_flight": flight.passengers.all().order_by('first'),
         "flight_id": flight_id
       })
      

