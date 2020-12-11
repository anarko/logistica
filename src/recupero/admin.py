from django.contrib import admin

# Register your models here.
from .models import Localidades,Empresas,Equipo

admin.site.register(Localidades)
admin.site.register(Empresas)
admin.site.register(Equipo)