from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *
from datetime import datetime
from django.core import serializers

#################################################################
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
###########
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
        lista_facultades = Facultad.objects.raw('SELECT DISTINCT f.cod_facultad, f.descripcion FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id =' + str(user) + ' AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_facultades = serializers.serialize('json', lista_facultades)
        lista_carreras = Carrera.objects.raw('SELECT DISTINCT c.cod_carrera, c.descripcion, c.cod_facultad_id as fk FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id = ' + str(user) + ' AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_carreras = serializers.serialize('json', lista_carreras)
        lista_asignaturas = Asignatura.objects.raw('SELECT asig.cod_asignatura, asig.descripcion FROM roducweb_asignatura asig, roducweb_asignatura_usuario asigu, roducweb_usuario u, roducweb_usuario_rol urol WHERE u.cod_usuario = ' + str(user) + ' AND u.cod_usuario = urol.cod_usuario_id AND urol.cod_rol_usuario_id = 2 AND urol.cod_usuario_rol = asigu.cod_usuario_rol_id AND asigu.cod_asignatura_id = asig.cod_asignatura  AND asigu.estado = 1')
        lista_asignaturas = serializers.serialize('json', lista_asignaturas)
        lista_planes = Plan_Estudio.objects.filter(estado = 1)
        lista_planes = serializers.serialize('json', lista_planes)
        lista_semestre = Semestre.objects.filter(estado = 1)
        lista_semestre = serializers.serialize('json', lista_semestre)
        lista_tipo_clase = Tipo_Clase.objects.filter(estado = 1)
        lista_tipo_clase = serializers.serialize('json', lista_tipo_clase)
        return JsonResponse({
            "lista_facultades": lista_facultades,
            "lista_carreras": lista_carreras,
            "lista_asignaturas": lista_asignaturas,
            "lista_planes": lista_planes,
            "lista_semestre": lista_semestre,
            "lista_tipo_clase": lista_tipo_clase,
        })

        
    

