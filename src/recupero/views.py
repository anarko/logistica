from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from .forms import UploadFileForm
from .form_functions import handle_uploaded_file
import json

def index(request):    
    if request.user.is_authenticated:
        template = loader.get_template('recupero/index.html')
        context = {}
        return HttpResponse(template.render(context,request))
    else:
        template = loader.get_template('recupero/login.html')
        context = {}
        return HttpResponse(template.render(context,request))
    
def login_user(request):
    try:
        username = request.POST['user']
        password = request.POST['pass']    
    except:
        context = {}
        template = loader.get_template('recupero/login.html')
        return HttpResponse(template.render(context,request))

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        context = {}
        template = loader.get_template('recupero/index.html')

    else:
        context = {}
        template = loader.get_template('recupero/login.html')

    return HttpResponse(template.render(context,request))
    

def logout_user(request):
    logout(request)
    context = {}
    template = loader.get_template('recupero/login.html')
    return HttpResponse(template.render(context,request))


def upload_files_form(request):

    if request.method == 'POST':
        if request.FILES:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                context = {'mensaje':"Archivo subido"}
                handle_uploaded_file(request.FILES['file'])
            else:
                context = {'mensaje':"Archivo NO subido"}
            
            template = loader.get_template('recupero/index.html')
            return HttpResponse(template.render(context,request))
        else:
            form = UploadFileForm() 
            template = loader.get_template('recupero/upload.html')
            context = {'form': form}
            return HttpResponse(json.dumps({'form': template.render(context,request)}))
    
    return(index(request))

    