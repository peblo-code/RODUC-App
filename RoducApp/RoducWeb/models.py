from tkinter import CASCADE
from django.db import models

# Create your models here.
class Usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)
    nombres_del_usuario = models.CharField(max_length=45)
    apellidos_del_usuario = models.CharField(max_length=45)
    direccion_email = models.CharField(max_length=60)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Rol_Usuario(models.Model):
    cod_rol_usuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Facultad(models.Model):
    cod_facultad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fecha_fundacion = models.DateField(auto_now=False)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Carrera(models.Model):
    cod_carrera = models.AutoField(primary_key=True)
    cod_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, blank=True)
    descripcion = models.CharField(max_length=45)
    duracion = models.IntegerField()
    titulo_obtenido = models.CharField(max_length=100)
    estado = models.IntegerField(null=True)
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Usuario_Rol(models.Model):
    cod_usuario_rol = models.AutoField(primary_key=True)
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)
    cod_rol_usuario = models.ForeignKey(Rol_Usuario, on_delete=models.CASCADE, blank=True)
    cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Auditoria(models.Model):
    cod_auditoria = models.AutoField(primary_key=True)
    tabla = models.CharField(max_length=100)
    accion = models.CharField(max_length=1)
    datos_viejos = models.CharField(max_length=5000)
    datos_nuevos = models.CharField(max_length=5000)
    usuario = models.CharField(max_length=45)
    fecha = models.DateField(auto_now=True)


class Auditoria_Sesiones(models.Model):
    cod_aud_sesiones = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    fecha = models.DateTimeField(auto_now=False)
    informacion = models.CharField(max_length=500)


class Semestre(models.Model):
    cod_semestre = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now = False, null=True)
    fecha_fin = models.DateField(auto_now = False, null=True)
    estado = models.IntegerField(null=True)
    alta_usuario = models.CharField(max_length=45, null=True)
    alta_fecha = models.DateTimeField(auto_now_add=True, null=True)
    modif_usuario = models.CharField(max_length=45, null=True)
    modif_fecha = models.DateTimeField(auto_now=True)


class Plan_Estudio(models.Model):
    cod_plan_estudio = models.AutoField(primary_key=True)
    cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Asignatura(models.Model):
    cod_asignatura = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    horas_catedra = models.IntegerField()
    curso = models.IntegerField()
    cod_semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, blank=True)
    cod_plan_estudio = models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE, blank=True)
    cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Asignatura_Usuario(models.Model):
    cod_asignatura_usuario = models.AutoField(primary_key=True)
    cod_usuario_rol = models.ForeignKey(Usuario_Rol, on_delete=models.CASCADE, blank=True, null = True)
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Tipo_Clase(models.Model):
    cod_tipo_clase = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)


class Unidad_Aprendizaje(models.Model):
    cod_unidad_aprendizaje = models.AutoField(primary_key=True)
    numero_unidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Contenido(models.Model):
    cod_contenido = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    cod_unidad_aprendizaje = models.ForeignKey(Unidad_Aprendizaje, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Instrumento_Evaluacion(models.Model):
    cod_instrumento_evaluacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Metodologia_Enseñanza(models.Model):
    cod_metodologia_enseñanza = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Recursos_Auxiliar(models.Model):
    cod_recurso_auxiliar = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Tipo_Eva(models.Model):
    cod_tipo_eva = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Trabajo_Autonomo(models.Model):
    cod_trabajo_autonomo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Cabecera_Planilla(models.Model):
    cod_cabecera_planilla = models.AutoField(primary_key=True)
    cod_tipo_clase = models.ForeignKey(Tipo_Clase, on_delete= models.CASCADE, blank=True, null=True)
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, blank=True)
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True)
    fecha_clase = models.DateField(auto_now=False)
    hora_entrada = models.TimeField(auto_now=False)
    hora_salida = models.TimeField(auto_now=False)
    fecha_vencimiento = models.DateField(auto_now=False)
    evaluacion = models.IntegerField()
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Contenidos_Dados(models.Model):
    cod_contenidos_dados = models.AutoField(primary_key=True)
    cod_cabecera_planilla = models.ForeignKey(Cabecera_Planilla, on_delete=models.CASCADE, blank=True)
    cod_contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Evaluaciones(models.Model):
    cod_evaluacion = models.AutoField(primary_key=True)
    cod_cabecera_planilla = models.ForeignKey(Cabecera_Planilla, on_delete=models.CASCADE, blank=True)
    cod_instrumento_evaluacion = models.ForeignKey(Instrumento_Evaluacion, on_delete=models.CASCADE, blank=True)
    cod_tipo_eva = models.ForeignKey(Tipo_Eva, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Trabajos_Utilizados(models.Model):
    cod_trabajos_utilizados = models.AutoField(primary_key=True)
    cod_cabecera_planilla = models.ForeignKey(Cabecera_Planilla, on_delete=models.CASCADE, blank=True)
    cod_trabajo_autonomo = models.ForeignKey(Trabajo_Autonomo, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Metodologia_Utilizada(models.Model):
    cod_metodologia_utilizada = models.AutoField(primary_key=True)
    cod_cabecera_planilla = models.ForeignKey(Cabecera_Planilla, on_delete=models.CASCADE, blank=True)
    cod_metodologia_enseñanza = models.ForeignKey(Metodologia_Enseñanza, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)

class Recursos_Utilizados(models.Model):
    cod_recursos_utilizados = models.AutoField(primary_key=True)
    cod_cabecera_planilla = models.ForeignKey(Cabecera_Planilla, on_delete=models.CASCADE, blank=True)
    cod_recurso_auxiliar = models.ForeignKey(Recursos_Auxiliar, on_delete=models.CASCADE, blank=True)
    estado = models.IntegerField()
    alta_usuario = models.CharField(max_length=45)
    alta_fecha = models.DateTimeField(auto_now_add=True)
    modif_usuario = models.CharField(max_length=45)
    modif_fecha = models.DateTimeField(auto_now=True)