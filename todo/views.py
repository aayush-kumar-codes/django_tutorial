from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
import json
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):

    def get(self, request):
        return HttpResponse("Hello, world!")

    @csrf_exempt
    def post(self, request):
        req = json.loads(request.body)
        print(req)
        todo = Todo(task=req["task"], created_at=timezone.now())
        todo.save()

        return HttpResponse(todo.id)
