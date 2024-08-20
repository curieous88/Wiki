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
         "passengers_all": Passenger.objects.all().order_by('first'),
         "passengers_in_flight": flight.passengers.all().order_by('first')
       })
      
def add_passengers_to_flight(request, flight_id):
    flight=Flight.objects.get(flight_id)
    if request.method == "POST":
      selected_passenger_ids = request.POST.getlist('add_passengers')
      add_passengers = Passenger.objects.filter(id__in=selected_passenger_ids)
      for passenger in add_passengers:
        flight.passengers.add(passenger)      
      return HttpResponseRedirect(reverse("flightinfo", args=(flight.id,)))
    else:
      return HttpResponseNotAllowed(['POST'])


