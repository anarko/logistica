from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import loader

def index(request):
    template = loader.get_template('recupero/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def logi(request):
    try:
        username = request.GET['user']
        password = request.GET['pass']
    except:
        return HttpResponse("login error")
        
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponse("login OK")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("login error")

