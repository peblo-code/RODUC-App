from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from html5lib import serialize
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *
from datetime import datetime
from django.core import serializers

#################################################################
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
#Auditoria Sesion
def auditar_sesion(request, user, info):
    nueva_sesion = Auditoria_Sesiones(
        nombre_usuario = user,
        fecha = datetime.now(),
        informacion = "Inicio de Sesion en " + info
    )
    nueva_sesion.save()

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer
    
class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "nombre_usuario"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class FacultadListAPIView(generics.ListAPIView):
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

class FacultadRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "cod_facultad"
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

class Cabecera_PlanillaCreateAPIView(generics.CreateAPIView):
    queryset = Cabecera_Planilla.objects.all()
    serializer_class = Cabecera_PlanillaSerializer

class EvaluacionesCreateAPIView(generics.CreateAPIView):
    queryset = Evaluaciones.objects.all()
    serializer_class = Evaluaciones_Serializer

class Contenidos_DadosCreateAPIView(generics.CreateAPIView):
    queryset = Contenidos_Dados.objects.all()
    serializer_class = Contenidos_DadosSerializer

class Recursos_UtilizadosCreateAPIView(generics.CreateAPIView):
    queryset = Recursos_Utilizados.objects.all()
    serializer_class = Recursos_UtilizadosSerializer

class Trabajos_UtilitizadosCreateAPIView(generics.CreateAPIView):
    queryset = Trabajos_Utilizados.objects.all()
    serializer_class = Trabajos_UtilizadosSerializer

class Metodologia_UtilizadaCreateAPIView(generics.CreateAPIView):
    queryset = Metodologia_Utilizada.objects.all()
    serializer_class = Metodologia_UtilizadaSerializer

#FUNCIONES
def validarSesion(request, user):
    if request.method == 'GET':
        if Usuario_Rol.objects.filter(estado = 1, cod_usuario = user, cod_rol_usuario = 2).exists():
            return JsonResponse({"respuesta": 1})
        else:
            return JsonResponse({"respuesta": 0})
@csrf_exempt
def auditoriaSesion(request, user, info):
    if request.method == "GET":
        auditar_sesion(request, user, info)
        return JsonResponse({"bandera": 1})
    else:
        return JsonResponse({"bandera": 0})

def listaFacultades_Carreras(request, user):
    if request.method == 'GET':
        fecha_actual = str(datetime.today())
        año_actual = fecha_actual[:(fecha_actual.find('-'))]
        
        #FACULTADES DEL USUARIO
        lista_facultades = Facultad.objects.raw('SELECT DISTINCT f.cod_facultad, f.descripcion FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id =' + str(user) + ' AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_facultades = serializers.serialize('json', lista_facultades)
        #CARRERAS DEL USUARIO
        lista_carreras = Carrera.objects.raw('SELECT DISTINCT c.cod_carrera, c.descripcion, c.cod_facultad_id as fk FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id = ' + str(user) + ' AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_carreras = serializers.serialize('json', lista_carreras)
        #ASIGNATURAS DEL USUARIO
        lista_asignaturas = Asignatura.objects.raw('SELECT asig.cod_asignatura, asig.descripcion FROM roducweb_asignatura asig, roducweb_asignatura_usuario asigu, roducweb_usuario u, roducweb_usuario_rol urol WHERE u.cod_usuario = ' + str(user) + ' AND u.cod_usuario = urol.cod_usuario_id AND urol.cod_rol_usuario_id = 2 AND urol.cod_usuario_rol = asigu.cod_usuario_rol_id AND asigu.cod_asignatura_id = asig.cod_asignatura  AND asigu.estado = 1')
        lista_asignaturas = serializers.serialize('json', lista_asignaturas)
        #LISTA DE PLANES
        lista_planes = Plan_Estudio.objects.filter(estado = 1)
        lista_planes = serializers.serialize('json', lista_planes)
        #LISTA DE SEMESTRES
        lista_semestre = Semestre.objects.filter(estado = 1)
        lista_semestre = serializers.serialize('json', lista_semestre)
        #LISTA DE TIPOS DE CLASE
        lista_tipo_clase = Tipo_Clase.objects.filter(estado = 1)
        lista_tipo_clase = serializers.serialize('json', lista_tipo_clase)
        #LISTA DE UNIDADES
        lista_unidad = Unidad_Aprendizaje.objects.raw("SELECT DISTINCT u.cod_unidad_aprendizaje, u.descripcion FROM roducweb_unidad_aprendizaje AS u, (SELECT * FROM roducweb_contenido AS cont WHERE cont.cod_contenido NOT IN (SELECT co.cod_contenido FROM roducweb_contenido AS co, roducweb_contenidos_dados AS cd, roducweb_cabecera_planilla AS c WHERE c.cod_cabecera_planilla = cd.cod_cabecera_planilla_id AND cd.cod_contenido_id = co.cod_contenido AND c.fecha_clase BETWEEN '" + str(año_actual) + "/01/01' AND '" + str(año_actual) + "/12/01' AND c.estado = 1 AND co.estado = 1 AND cd.estado = 1) AND cont.estado = 1) as con WHERE u.cod_unidad_aprendizaje = con.cod_unidad_aprendizaje_id")
        lista_unidad = serializers.serialize('json', lista_unidad)
        #LISTA DE CONTENIDOS
        lista_contenido = Contenido.objects.raw("SELECT * FROM roducweb_contenido as cont WHERE cont.cod_contenido NOT IN (SELECT co.cod_contenido FROM roducweb_contenido as co ,roducweb_contenidos_dados as cd ,roducweb_cabecera_planilla as c WHERE c.cod_cabecera_planilla = cd.cod_cabecera_planilla_id and cd.cod_contenido_id = co.cod_contenido and c.fecha_clase BETWEEN '" + str(año_actual) + "/01/01' and '" + str(año_actual) + "/12/01'  and c.estado = 1 and co.estado = 1 and cd.estado = 1) and cont.estado = 1")
        lista_contenido = serializers.serialize('json', lista_contenido)
        #INSTRUMENTO DE EVALUACION
        lista_instrumento_evaluacion = Instrumento_Evaluacion.objects.filter(estado = 1)
        lista_instrumento_evaluacion = serializers.serialize('json', lista_instrumento_evaluacion)
        #LISTA RECURSOS AUXILIARES
        lista_recurso = Recursos_Auxiliar.objects.filter(estado = 1)
        lista_recurso = serializers.serialize('json', lista_recurso)
        #TIPO EVALUACION 
        lista_tipo_evaluacion = Tipo_Eva.objects.filter(estado = 1)
        lista_tipo_evaluacion = serializers.serialize('json', lista_tipo_evaluacion)
        #lISTA TRABAJO AUTONOMO
        lista_trabajo = Trabajo_Autonomo.objects.filter(estado = 1)
        lista_trabajo = serializers.serialize('json', lista_trabajo)
        #LISTA DE METODOLOGIA
        lista_metodologia = Metodologia_Enseñanza.objects.filter(estado = 1)
        lista_metodologia = serializers.serialize('json', lista_metodologia)
        return JsonResponse({
            "lista_facultades": lista_facultades,
            "lista_carreras": lista_carreras,
            "lista_asignaturas": lista_asignaturas,
            "lista_planes": lista_planes,
            "lista_semestre": lista_semestre,
            "lista_tipo_clase": lista_tipo_clase,
            "lista_unidad": lista_unidad,
            "lista_contenido": lista_contenido,
            "lista_instrumento_evaluacion": lista_instrumento_evaluacion,
            "lista_recurso": lista_recurso,
            "lista_tipo_evaluacion": lista_tipo_evaluacion,
            "lista_trabajo": lista_trabajo,
            "lista_metodologia": lista_metodologia,
        })

def historialReportes(request, user):
    if request.method == 'GET':
        lista_cabeceras = Cabecera_Planilla.objects.filter(estado = 1, cod_usuario_id = user).order_by('fecha_clase')
        lista_cabeceras = serializers.serialize('json', lista_cabeceras)
        return JsonResponse({"lista_cabeceras": lista_cabeceras})