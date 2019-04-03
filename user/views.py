from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

import json
from passlib.hash import pbkdf2_sha256

from user.models import User

@csrf_exempt
def login(request):
    return HttpResponse("")


@csrf_exempt
def register(request):

    if not request.method == "POST":
        return HttpResponseNotAllowed("POST")

    req = json.loads(request.body)

    # add validations here if need. for now i am skipping that

    username = req["username"]
    password = req["password"]

    user = User(username=username,password=pbkdf2_sha256.hash(password))
    user.save()
    return HttpResponse(user.id)
