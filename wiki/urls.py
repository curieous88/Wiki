from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("landing", views.landing, name="landing"),
    path("<str:name>", views.greet, name="greet"),
    # path("homepage", views.homepage, name="homepage")
]
