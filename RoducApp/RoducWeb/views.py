import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from RoducWeb.models import *
import time #sacar hora
from restapi.views import Auditoria

#NOTAS
#1-Serializers solo se puede con metodo Filter, con get no funciona

###########################################################################################
#funciones varias
def generar_saludo():
    hora_actual = int((time.strftime('%H', time.localtime())))
    if (hora_actual >= 0 and hora_actual < 12):
        mensaje_bienvenida = 'Buenos Dias'
    elif (hora_actual >= 12 and hora_actual < 19):
        mensaje_bienvenida = 'Buenas Tardes'
    else:
        mensaje_bienvenida = 'Buenas Noches'
    return mensaje_bienvenida
###########################################################################################

# Create your views here.

def login(request):
    if request.method == 'GET':
        if (request.session.get("usuario_conectado")):
            return redirect("inicio")
        else:
            return render(request, 'login.html')
    if request.method == 'POST':
        nom_usuario = request.POST.get('usuario')
        contraseña_usuario = request.POST.get('contraseña')
        usuario_actual = Usuario.objects.filter(nombre_usuario = nom_usuario).exists()
        if usuario_actual == True: #se verifica si el usuario existe
            rol_usuario = Usuario_Rol.objects.filter(cod_usuario = Usuario.objects.get(nombre_usuario = nom_usuario).cod_usuario, estado = 1, cod_rol_usuario = 1).exists()
            datos_usuario = Usuario.objects.get(nombre_usuario = nom_usuario)
            if rol_usuario:
                if (datos_usuario.contraseña == contraseña_usuario):
                    request.session["usuario_conectado"] = datos_usuario.nombre_usuario
                    request.session["nombre_del_usuario"] = datos_usuario.nombres_del_usuario 
                    request.session["correo_usuario"] = datos_usuario.direccion_email
                    Auditoria(request,"usuario_conectado", 'Inicia Sesion')
                    return redirect("inicio")
                else:
                    return render(request, "login.html", {"mensaje_error": "La contraseña ingresada es incorrecta."})
            else:
                return render(request, "login.html", {"mensaje_error": "El usuario no cuenta con los permisos necesarios para acceder."})
        else:
            return render(request, "login.html", {"mensaje_error": "El usuario ingresado no existe."})

def cerrar_sesion(request):
    request.session.flush()
    return redirect("login")

def inicio(request):
    mensaje_bienvenida = generar_saludo()
    return render(request, "inicio.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                           "nombre_usuario": request.session.get("nombre_del_usuario"),
                                           "direccion_email": request.session.get("correo_usuario"),
                                           "inicio": 'S',
                                           "mensaje_bienvenida": mensaje_bienvenida})


def usuario(request, usuario_actual = 0):
    mensaje_bienvenida = generar_saludo()
    lista_usuarios = Usuario.objects.filter(estado = 1)
    return render(request, "usuarios/usuario.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                     "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                     "direccion_email":request.session.get("correo_usuario"),
                                                     "mensaje_bienvenida": mensaje_bienvenida,
                                                     "lista_usuarios":lista_usuarios,
                                                     "usuario_actual": usuario_actual})


def facultad(request):
    mensaje_bienvenida = generar_saludo()
    lista_facultad = Facultad.objects.filter(estado = 1)
    return render(request, "facultad/facultad.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                     "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                     "direccion_email":request.session.get("correo_usuario"),
                                                     "mensaje_bienvenida": mensaje_bienvenida,
                                                     "lista_facultad": lista_facultad})
def agregar_facultad(request):
    if request.method == 'POST':
        facultad_nueva = Facultad(
            descripcion = request.POST.get('descripcion'),
            fecha_fundacion = request.POST.get('fecha'),
            estado = 1
        )
        facultad_nueva.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Exito"})
        return respuesta
    return render(request, "facultad/facultad.html")
def detalle_facultad(request):
    if request.method == 'GET':
        detalle = Facultad.objects.filter(cod_facultad = request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        print(detalle)
        return JsonResponse({"detalle": detalle})

def carrera(request):
    return render(request, "carrera/carrera.html")
    
def plan_estudio(request):
    return render(request, "plan_estudio/plan_estudio.html")

def semestre(request):
    return render(request, "semestre/semestre.html")

def asignatura(request):
    return render(request, "asignatura/asignatura.html")
