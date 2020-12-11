from django.db import models

# Create your models here.
class Localidades(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Empresas(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Equipo(models.Model):
    codm = models.CharField(max_length=50, unique=True)
    nro_lote = models.IntegerField()
    observaciones = models.CharField(max_length=255)
    nro_tarea = models.IntegerField()
    nro_cuenta = models.IntegerField()
    nya_cliente = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    localidad_contable = models.ForeignKey(Localidades, on_delete=models.PROTECT, related_name='localidad_contable',default='')
    localidad_retiro = models.ForeignKey(Localidades, on_delete=models.PROTECT, related_name='localidad_retiro',default='')
    codigo_postal = models.CharField(max_length=20,default=None)
    tel1 = models.CharField(max_length=255,default=None)
    tel2 = models.CharField(max_length=255,default=None)
    tel3 = models.CharField(max_length=255,default=None)
    tel4 = models.CharField(max_length=255,default=None)
    email = models.CharField(max_length=255,default=None)
    recuperado = models.BooleanField(default=False)
    base_nro_serie = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    
    

