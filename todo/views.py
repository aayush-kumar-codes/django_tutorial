from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt    
def addTodo(request):
    if request.method == "POST":
        return HttpResponse("OK")
    else:
        return HttpResponseNotAllowed("POST")
