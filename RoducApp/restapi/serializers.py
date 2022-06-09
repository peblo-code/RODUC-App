from pyexpat import model
from rest_framework import serializers
from RoducWeb.models import *

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'cod_usuario', 
            'nombre_usuario',
            'contraseña',
            'nombres_del_usuario',
            'apellidos_del_usuario', 
            'direccion_email',
            'estado', 
            'alta_usuario', 
            'alta_fecha', 
            'modif_usuario',
            'modif_fecha',
        ]

class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'cod_usuario', 
            'nombre_usuario',
            'contraseña',
            'nombres_del_usuario',
            'apellidos_del_usuario', 
            'direccion_email',
            'estado', 
            'alta_usuario', 
            'alta_fecha', 
            'modif_usuario',
            'modif_fecha',
        ]
        

class Usuario_RolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Rol
        fields = [
            'cod_usuario_rol',
            'estado',
            'alta_usuario',
            'alta_fecha',
            'modif_usuario',
            'modif_fecha',
            'cod_rol_usuario_id',
            'cod_usuario_id',
            'cod_carrera_id',
        ]

class FacultadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = [
            'cod_facultad',
            'descripcion',
            'fecha_fundacion',
            'estado',
            'alta_usuario',
            'alta_fecha',
            'modif_usuario',
            'modif_fecha',
        ]

class Auditoria_SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria_Sesiones
        fields = [
            'cod_aud_sesiones',
            'nombre_usuario',
            'fecha',
            'informacion',
        ]

class Cabecera_PlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabecera_Planilla
        fields = [
            'cod_cabecera_planilla',
            'cod_tipo_clase',
            'cod_asignatura',
            'cod_usuario',
            'fecha_clase',
            'hora_entrada',
            'hora_salida',
            'fecha_vencimiento',
            'evaluacion',
            'estado',
            'alta_usuario',
            'alta_fecha',
            'modif_usuario',
            'modif_fecha',
        ]