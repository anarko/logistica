from django.contrib import admin

# Register your models here.
from .models import Localidades,Empresas,Equipo,ResultadoLlamada,Llamadas

admin.site.register(Localidades)
admin.site.register(Empresas)
admin.site.register(Equipo)
admin.site.register(ResultadoLlamada)
admin.site.register(Llamadas)
