from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
import json
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world!")


@csrf_exempt
def addTodo(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)
        todo = Todo(task=req["task"], created_at=timezone.now())
        todo.save()

        return HttpResponse(todo.id)
    else:
        return HttpResponseNotAllowed("POST")
