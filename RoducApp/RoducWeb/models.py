from django.db import models

# Create your models here.

class Usuario(models.Model):
    cod_usuario           = models.AutoField(primary_key = True)
    nombre_usuario        = models.CharField(max_length  = 45)
    contraseña            = models.CharField(max_length  = 45)
    nombres_del_usuario   = models.CharField(max_length  = 45)
    apellidos_del_usuario = models.CharField(max_length  = 45)
    direccion_email       = models.CharField(max_length  = 60)
    estado                = models.IntegerField()
    alta_usuario          = models.CharField(max_length  = 45)
    alta_fecha            = models.DateTimeField(auto_now_add = True)
    modif_usuario         = models.CharField(max_length  = 45)
    modif_fecha           = models.DateTimeField(auto_now = True)

class Rol_Usuario(models.Model):
    cod_rol_usuario       = models.AutoField(primary_key = True)
    descripcion           = models.CharField(max_length = 45)
    estado                = models.IntegerField()
    alta_usuario          = models.CharField(max_length = 45)
    alta_fecha            = models.DateTimeField(auto_now_add = True)
    modif_usuario         = models.CharField(max_length = 45)
    modif_fecha           = models.DateTimeField(auto_now = True)