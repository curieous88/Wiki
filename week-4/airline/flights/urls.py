from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="flights"),
    path("<int:flight_id>", views.flightinfo, name="flightinfo"),
]
