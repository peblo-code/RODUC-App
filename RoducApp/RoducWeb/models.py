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

class Facultad(models.Model):
    cod_facultad         = models.AutoField(primary_key = True)
    descripcion          = models.CharField(max_length = 100)
    fecha_fundacion      = models.DateField(auto_now = False)
    estado                = models.IntegerField()
    alta_usuario          = models.CharField(max_length = 45)
    alta_fecha            = models.DateTimeField(auto_now_add = True)
    modif_usuario         = models.CharField(max_length = 45)
    modif_fecha           = models.DateTimeField(auto_now = True)

class Carrera(models.Model):
    cod_carrera           = models.AutoField(primary_key = True)
    cod_faculad           = models.ForeignKey(Facultad, on_delete = models.CASCADE, blank = True)
    descripcion           = models.CharField(max_length = 45)
    duracion              = models.IntegerField()
    titulo_obtenido       = models.CharField(max_length = 100)
    alta_usuario          = models.CharField(max_length = 45)
    alta_fecha            = models.DateTimeField(auto_now_add = True)
    modif_usuario         = models.CharField(max_length = 45)
    modif_fecha           = models.DateTimeField(auto_now = True) 

class Usuario_Rol(models.Model):
    cod_usuario_rol       = models.AutoField(primary_key = True)
    cod_usuario           = models.ForeignKey(Usuario, on_delete = models.CASCADE, blank = True)
    cod_rol_usuario       = models.ForeignKey(Rol_Usuario, on_delete = models.CASCADE, blank = True)
    cod_carrera           = models.ForeignKey(Carrera, on_delete = models.CASCADE, blank = True, null = True)
    estado                = models.IntegerField()
    alta_usuario          = models.CharField(max_length = 45)
    alta_fecha            = models.DateTimeField(auto_now_add = True)
    modif_usuario         = models.CharField(max_length = 45)
    modif_fecha           = models.DateTimeField(auto_now = True)


class Auditoria(models.Model):
    cod_auditoria         = models.AutoField(primary_key = True)
    tabla                 = models.CharField(max_length = 100)
    accion                = models.CharField(max_length = 1)
    datos_viejos          = models.CharField(max_length = 5000)
    datos_nuevos          = models.CharField(max_length = 5000)
    usuario               = models.CharField(max_length = 45)
    fecha                 = models.DateField(auto_now = True)

class Auditoria_Sesiones(models.Model):
    cod_aud_sesiones      = models.AutoField(primary_key  = True)
    nombre_usuario        = models.CharField(max_length   = 45)
    fecha                 = models.DateTimeField(auto_now = False)
    informacion           = models.CharField(max_length   = 500)


