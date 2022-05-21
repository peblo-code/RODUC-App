from curses.ascii import HT
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

class Usuario_RolRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "cod_usuario_id"
    #queryset = Usuario_Rol.objects.filter(estado = 1, cod_rol_usuario = 2).first()
    #queryset = Usuario_Rol.objects.all()
    #queryset = Usuario_Rol.objects.filter()
    queryset = Usuario_Rol.objects.raw('select * from roducweb_usuario_rol where cod_rol_usuario_id = 2 limit 1')
    serializer_class = Usuario_RolDetailSerializer

class FacultadListAPIView(generics.ListAPIView):
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

class FacultadRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "cod_facultad"
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

class AuditoriaSesionesCreateAPIView(generics.CreateAPIView):
    queryset = Auditoria_Sesiones.objects.all()
    serializer_class = Auditoria_SesionesSerializer


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
        print("No entro a get")
        return JsonResponse({"bandera": 0})

def listaFacultades_Carreras(request, user):
    if request.method == 'GET':
        lista_facultades = Facultad.objects.raw('SELECT DISTINCT f.cod_facultad, f.descripcion FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id = 1 AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_facultades = serializers.serialize('json', lista_facultades)
        lista_carreras = Carrera.objects.raw('SELECT DISTINCT c.cod_carrera, c.descripcion FROM roducweb_carrera as c, roducweb_facultad as f, roducweb_usuario_rol as u WHERE u.cod_carrera_id = c.cod_carrera AND c.cod_facultad_id = f.cod_facultad AND u.cod_usuario_id = 1 AND u.cod_rol_usuario_id = 2 AND u.estado = 1')
        lista_carreras = serializers.serialize('json', lista_carreras)
        return JsonResponse({
            "lista_facultades": lista_facultades,
            "lista_carreras": lista_carreras
        })

        
    

