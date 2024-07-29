
from django.shortcuts import render

tasks = ["Wash clothes", "make plant hanger", "order groceries"]

# Create your views here.
def index(request):
     return render(request, "tasks/index.html", {
          "tasks" : tasks
          })

def add(request):
     return render(request, "tasks/add.html")