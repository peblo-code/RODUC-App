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
        ]

class Evaluaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluaciones
        fields = [
            'cod_evaluacion',
            'cod_cabecera_planilla',
            'cod_tipo_eva',
            'cod_instrumento_evaluacion',
            'estado',
            'alta_usuario',
        ]

class Contenidos_DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenidos_Dados
        fields = [
            'cod_contenidos_dados',
            'cod_cabecera_planilla',
            'cod_contenido',
            'estado',
            'alta_usuario',
        ]

class Recursos_UtilizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recursos_Utilizados
        fields = [
            'cod_recursos_utilizados',
            'cod_cabecera_planilla',
            'cod_recurso_auxiliar',
            'estado',
            'alta_usuario',
        ]

class Trabajos_UtilizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajos_Utilizados
        fields = [
            'cod_trabajos_utilizados',
            'cod_cabecera_planilla',
            'cod_trabajo_autonomo',
            'estado',
            'alta_usuario',
        ]

class Metodologia_UtilizadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodologia_Utilizada
        fields = [
            'cod_metodologia_utilizada',
            'cod_cabecera_planilla',
            'cod_metodologia_enseñanza',
            'estado',
            'alta_usuario',
        ]