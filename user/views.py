from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

import json
from passlib.hash import pbkdf2_sha256

from user.models import User


@csrf_exempt
def login(request):
    if not request.method == "POST":
        return HttpResponseNotAllowed("POST")

    req = json.loads(request.body)

    # add validations here if need. for now i am skipping that

    username = req["username"]
    password = req["password"]

    users = User.objects.filter(username=username)
    if users:
        user = users.first()
        if pbkdf2_sha256.verify(password, user.password):
            return HttpResponse("OK")
        else:
            return HttpResponseServerError()
    else:
        return HttpResponseServerError()


@csrf_exempt
def register(request):

    if not request.method == "POST":
        return HttpResponseNotAllowed("POST")

    req = json.loads(request.body)

    # add validations here if need. for now i am skipping that

    username = req["username"]
    password = req["password"]

    user = User(username=username, password=pbkdf2_sha256.hash(password))
    user.save()
    return HttpResponse(user.id)
