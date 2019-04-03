from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    return HttpResponse("")


@csrf_exempt
def register(request):
    return HttpResponse("")
