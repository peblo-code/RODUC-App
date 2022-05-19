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
            'cod_usuario',
            'cod_rol_usuario',
            'estado',
            'alta_usuario',
            'alta_fecha',
            'modif_usuario',
            'modif_fecha',
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