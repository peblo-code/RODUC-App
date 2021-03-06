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

class Auditoria_SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria_Sesiones
        fields = [
            'cod_aud_sesiones',
            'nombre_usuario',
            'fecha',
            'informacion',
        ]