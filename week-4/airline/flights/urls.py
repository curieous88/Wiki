from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="flights"),
    path("<int:flight_id>", views.flightinfo, name="flightinfo"),
    path("<int:flight_id>/add_passengers_to_flight", views.add_passengers_to_flight, name="add_passengers_to_flight")
]
