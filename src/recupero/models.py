from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.
class Localidades(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Empresas(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Equipo(models.Model):
    codm_barras = models.CharField(max_length=50, unique=True,default=None)
    codm = models.CharField(max_length=50, unique=True,default=None)
    id_c = models.IntegerField(default=0)
    nro_serie_barras = models.CharField(max_length=50, unique=True,default=None)
    nro_serie = models.CharField(max_length=50, unique=True,default=None)
    nro_tarea_barras = models.CharField(max_length=50, unique=True, default=None)
    nro_tarea = models.IntegerField()
    nro_cuenta = models.IntegerField()
    nya_cliente = models.CharField(max_length=255,default=None)
    id_actividad = models.CharField(max_length=50, default=None)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    telefonos = models.CharField(max_length=500,default=None)
    domicilio = models.CharField(max_length=500,default=None)
    localidad = models.ForeignKey(Localidades, on_delete=models.PROTECT, related_name='localidad',default=None)
    codigo_postal = models.CharField(max_length=20,default=None)
    item_tarea = models.CharField(max_length=255,default=None)
    fecha_envio = models.DateField(default=None)
    fecha_creacion = models.DateField(default=None)
    zona = models.CharField(max_length=255,default=None)
    nombre_cartera = models.CharField(max_length=255,default=None)
    notas = models.CharField(max_length=255,default=None)
    localidad_contable = models.ForeignKey(Localidades, on_delete=models.PROTECT, related_name='localidad_contable',default=None)
    correo = models.CharField(max_length=255,default=None)
    email = models.CharField(max_length=255,default=None)
    proveedor = models.CharField(max_length=255,default=None)
    
class Llamadas(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    fecha_llamada = models.DateField(default=None)
    fecha_retiro = models.DateField(default=None)
    hora_inicio_retiro = models.TimeField(default=None)
    hora_fin_retiro = models.TimeField(default=None)
    entre_calles = models.CharField(max_length=255,default=None)
    observacion = models.CharField(max_length=255,default=None)
    resultado = models.ForeignKey(ResultadoLlamada, on_delete=models.PROTECT)

class ResultadoLlamada(models.Model):
    resultado = models.CharField(max_length=255,default=None)
    n1 = models.CharField(max_length=255,default=None)
    n2 = models.CharField(max_length=255,default=None)
    n3 = models.CharField(max_length=255,default=None)
    n4 = models.CharField(max_length=255,default=None)
