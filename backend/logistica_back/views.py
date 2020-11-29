from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def login(request):
    username = request.GET['user']
    password = request.GET['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        return HttpResponse("login OK")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("login error")

