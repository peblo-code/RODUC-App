from datetime import datetime
from doctest import debug_script
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from RoducWeb.models import *
import time  # sacar hora

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator


# NOTAS
# 1-Serializers solo se puede con metodo Filter, con get no funciona

###########################################################################################
# funciones varias
def generar_saludo():
    hora_actual = int((time.strftime('%H', time.localtime())))
    if (hora_actual >= 0 and hora_actual < 12):
        mensaje_bienvenida = 'Buenos Días'
    elif (hora_actual >= 12 and hora_actual < 19):
        mensaje_bienvenida = 'Buenas Tardes'
    else:
        mensaje_bienvenida = 'Buenas Noches'
    return mensaje_bienvenida

# auditar sesiones
def auditar_sesion(request, info):
    nueva_sesion = Auditoria_Sesiones(
        nombre_usuario=request.session.get("usuario_conectado"),
        fecha=datetime.now(),
        informacion=info
    )
    nueva_sesion.save()
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
        usuario_actual = Usuario.objects.filter(
            nombre_usuario=nom_usuario).exists()
        if usuario_actual == True:  # se verifica si el usuario existe
            rol_usuario = Usuario_Rol.objects.filter(cod_usuario=Usuario.objects.get(
                nombre_usuario=nom_usuario).cod_usuario, estado=1, cod_rol_usuario=1).exists()
            datos_usuario = Usuario.objects.get(nombre_usuario=nom_usuario)
            if rol_usuario:
                if (datos_usuario.contraseña == contraseña_usuario):
                    request.session["usuario_conectado"] = datos_usuario.nombre_usuario
                    request.session["nombre_del_usuario"] = datos_usuario.nombres_del_usuario
                    request.session["correo_usuario"] = datos_usuario.direccion_email
                    auditar_sesion(request, 'Inicia Sesion')
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


def usuario(request):
    mensaje_bienvenida = generar_saludo()
    lista_usuarios = Usuario.objects.filter(estado=1)
    lista_roles = Rol_Usuario.objects.filter(estado=1)
    lista_facultades = Facultad.objects.filter(estado=1)
    return render(request, "usuarios/usuario.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                     "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                     "direccion_email": request.session.get("correo_usuario"),
                                                     "mensaje_bienvenida": mensaje_bienvenida,
                                                     "lista_usuarios": lista_usuarios,
                                                     "lista_roles": lista_roles,
                                                     "lista_facultades": lista_facultades})


def agregar_usuario(request):
    if request.method == 'POST':
        usuario_nuevo = Usuario(
            nombre_usuario=request.POST.get('username'),
            contraseña=request.POST.get('password'),
            nombres_del_usuario=request.POST.get('nombres'),
            apellidos_del_usuario=request.POST.get('apellidos'),
            direccion_email=request.POST.get('correo'),
            estado=1,
            alta_usuario=request.session.get('usuario_conectado')
        )
        usuario_nuevo.save()
        usuario_nuevo = Usuario.objects.filter(nombre_usuario=usuario_nuevo.nombre_usuario)
        usuario_nuevo = serializers.serialize("json", usuario_nuevo)
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito",
                                  "usuario": usuario_nuevo})
        return respuesta


def detalle_usuario(request):
    if request.method == 'GET':
        detalle = Usuario.objects.filter(cod_usuario=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_usuario(request):
    if request.method == "POST":
        usuario_actualizar = Usuario.objects.get(cod_usuario=request.POST.get("codigo"))
        usuario_actualizar.nombres_del_usuario = request.POST.get("nombres")
        usuario_actualizar.apellidos_del_usuario = request.POST.get("apellidos")
        usuario_actualizar.direccion_email = request.POST.get("correo")
        usuario_actualizar.estado = 1
        usuario_actualizar.modif_usuario = request.session.get("usuario_conectado")
        usuario_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_usuario(request):
    if request.method == "POST":
        usuario_eliminar = Usuario.objects.get(cod_usuario=request.POST.get("codigo"))
        usuario_eliminar.estado = 0
        usuario_eliminar.modif_usuario = request.session.get("usuario_conectado")
        usuario_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def facultad(request):
    mensaje_bienvenida = generar_saludo()
    lista_facultad = Facultad.objects.filter(estado=1)
    return render(request, "facultad/facultad.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario"),
                                                      "mensaje_bienvenida": mensaje_bienvenida,
                                                      "lista_facultad": lista_facultad})


def agregar_facultad(request):
    if request.method == 'POST':
        facultad_nueva = Facultad(
            descripcion=request.POST.get('descripcion'),
            fecha_fundacion=request.POST.get('fecha'),
            estado=1,
            alta_usuario=request.session.get("usuario_conectado")
        )
        facultad_nueva.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


def detalle_facultad(request):
    if request.method == 'GET':
        detalle = Facultad.objects.filter(cod_facultad=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_facultad(request):
    if request.method == 'POST':
        facultad_actualizar = Facultad.objects.get(cod_facultad=request.POST.get("codigo"))
        facultad_actualizar.descripcion = request.POST.get("nombre")
        facultad_actualizar.fecha_fundacion = request.POST.get("fecha")
        facultad_actualizar.estado = 1
        facultad_actualizar.modif_usuario = request.session.get("usuario_conectado")
        facultad_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_facultad(request):
    if request.method == "POST":
        print(request.POST.get("codigo"))
        facultad_eliminar = Facultad.objects.get(cod_facultad=request.POST.get("codigo"))
        facultad_eliminar.estado = 0
        facultad_eliminar.modif_usuario = request.session.get("usuario_conectado")
        facultad_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def carrera(request):
    lista_carreras = Carrera.objects.filter(estado = 1)
    lista_facultades = Facultad.objects.filter(estado = 1)
    return render(request, "carrera/carrera.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario"),
                                                      "mensaje_bienvenida": generar_saludo(),
                                                      "lista_facultades": lista_facultades,
                                                      "lista_carreras": lista_carreras})


def agregar_carrera(request):
    if request.method == "POST":
        carrera_nueva = Carrera(
            descripcion = request.POST.get("descripcion"),
            duracion = request.POST.get("duracion"),
            titulo_obtenido = request.POST.get("titulo"),
            cod_facultad_id = request.POST.get("facultad"),
            alta_usuario = request.session.get("usuario_conectado"),
            estado = 1
        )
        carrera_nueva.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


def detalle_carrera(request):
    if request.method == 'GET':
        detalle = Carrera.objects.filter(cod_carrera=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_carrera(request):
    if request.method == "POST":
        carrera_actualizar = Carrera.objects.get(cod_carrera = request.POST.get("codigo"))
        carrera_actualizar.descripcion = request.POST.get("descripcion")
        carrera_actualizar.duracion = request.POST.get("duracion")
        carrera_actualizar.titulo_obtenido = request.POST.get("titulo")
        carrera_actualizar.cod_facultad_id = request.POST.get("facultad")
        carrera_actualizar.modif_usuario = request.session.get("usuario_conectado")
        carrera_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_carrera(request):
    if request.method == "POST":
        carrera_eliminar = Carrera.objects.get(cod_carrera = request.POST.get("codigo"))
        carrera_eliminar.estado = 0
        carrera_eliminar.modif_usuario = request.session.get("usuario_conectado")
        carrera_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def plan_estudio(request):
    lista_carreras = Carrera.objects.filter(estado=1)
    lista_facultades = Facultad.objects.filter(estado=1)
    lista_planes = Plan_Estudio.objects.filter(estado=1)
    return render(request, "plan_estudio/plan_estudio.html", {"mensaje_bienvenida": generar_saludo(),
                                                              "usuario_conectado": request.session.get("usuario_conectado"),
                                                              "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                              "direccion_email": request.session.get("correo_usuario"),
                                                              "lista_carreras": lista_carreras,
                                                              "lista_facultades": lista_facultades,
                                                              "lista_planes": lista_planes})


def agregar_plan(request):
    if request.method == "POST":
        nuevo_plan = Plan_Estudio(
            descripcion=request.POST.get("descripcion"),
            estado=1,
            alta_usuario=request.session.get("usuario_conectado"),
            cod_carrera_id=request.POST.get("carrera")
        )
        nuevo_plan.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


def detalle_plan(request):
    if request.method == 'GET':
        detalle = Plan_Estudio.objects.filter(cod_plan_estudio=request.GET.get("codigo"))
        carrera = Plan_Estudio.objects.get(cod_plan_estudio=request.GET.get("codigo")).cod_carrera_id
        facultad = Facultad.objects.get(cod_facultad=(Carrera.objects.get(cod_carrera=carrera).cod_facultad_id)).cod_facultad
        detalle = serializers.serialize("json", detalle)

        #facultad = Facultad.objects.get(cod_facultad = (Carrera.objects.get(detalle.cod_facultad).cod_facultad))
        return JsonResponse({"detalle": detalle,
                             "facultad": facultad})


def actualizar_plan(request):
    if request.method == "POST":
        plan_actualizar = Plan_Estudio.objects.get(
            cod_plan_estudio=request.POST.get("codigo"))
        plan_actualizar.descripcion = request.POST.get("descripcion")
        plan_actualizar.cod_carrera_id = request.POST.get("carrera")
        plan_actualizar.modif_usuario = request.session.get("usuario_conectado")
        plan_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_plan(request):
    if request.method == "POST":
        plan_eliminar = Plan_Estudio.objects.get(cod_plan_estudio=request.POST.get("codigo"))
        plan_eliminar.estado = 0
        plan_eliminar.modif_usuario = request.session.get("usuario_conectado")
        plan_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def semestre(request):
    lista_semestre = Semestre.objects.filter(estado=1)
    return render(request, "semestre/semestre.html", {"lista_semestre": lista_semestre,
                                                      "mensaje_bienvenida": generar_saludo(),
                                                      "usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario")})


def agregar_semestre(request):
    if request.method == 'POST':
        nuevo_semestre = Semestre(
            descripcion=request.POST.get("descripcion"),
            fecha_inicio = request.POST.get("fecha_inicio"),
            fecha_fin = request.POST.get("fecha_fin"),
            alta_usuario=request.session.get("usuario_conectado"),
            estado = 1
        )
        nuevo_semestre.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


def detalle_semestre(request):
    if request.method == 'GET':
        detalle = Semestre.objects.filter(cod_semestre=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_semestre(request):
    if request.method == 'POST':
        print(request.POST.get("codigo"))
        semestre_actualizar = Semestre.objects.get(cod_semestre=request.POST.get("codigo"))
        semestre_actualizar.descripcion = request.POST.get("descripcion")
        semestre_actualizar.fecha_inicio = request.POST.get("fecha_inicio")
        semestre_actualizar.fecha_fin = request.POST.get("fecha_fin")
        semestre_actualizar.modif_usuario = request.session.get("usuario_conectado")
        semestre_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_semestre(request):
    if request.method == "POST":
        semestre_eliminar = Semestre.objects.get(cod_semestre=request.POST.get("codigo"))
        semestre_eliminar.estado = 0
        semestre_eliminar.modif_usuario = request.session.get("usuario_conectado")
        semestre_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def asignatura(request):
    lista_carreras = Carrera.objects.filter(estado = 1)
    lista_planes = Plan_Estudio.objects.filter(estado = 1)
    lista_semestres = Semestre.objects.filter(estado = 1)
    lista_asignaturas = Asignatura.objects.filter(estado = 1)
    return render(request, "asignatura/asignatura.html", {"mensaje_bienvenida": generar_saludo(),
                                                          "usuario_conectado": request.session.get("usuario_conectado"),
                                                          "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                          "lista_carreras": lista_carreras,
                                                          "lista_planes": lista_planes,
                                                          "lista_semestres": lista_semestres,
                                                          "lista_asignaturas": lista_asignaturas})


def agregar_asignatura(request):
    asignatura_nueva = Asignatura(
        descripcion = request.POST.get("descripcion"),
        horas_catedra = request.POST.get("horas"),
        curso = request.POST.get("curso"),
        estado = 1,
        alta_usuario = request.session.get("usuario_conectado"),
        cod_carrera_id = request.POST.get("carrera"),
        cod_plan_estudio_id = request.POST.get("plan"),
        cod_semestre_id = request.POST.get("semestre")
    )
    asignatura_nueva.save()
    respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
    return respuesta


def detalle_asignatura(request):
    if request.method == 'GET':
        detalle = Asignatura.objects.filter(cod_asignatura=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_asignatura(request):
    if request.method == "POST":
        asignatura_actualizar = Asignatura.objects.get(cod_asignatura = request.POST.get("codigo"))
        asignatura_actualizar.descripcion = request.POST.get("descripcion")
        asignatura_actualizar.horas_catedra = request.POST.get("horas")
        asignatura_actualizar.curso = request.POST.get("curso")
        asignatura_actualizar.cod_carrera_id = request.POST.get("carrera")
        asignatura_actualizar.cod_plan_estudio_id = request.POST.get("plan")
        asignatura_actualizar.cod_semestre_id = request.POST.get("semestre")
        asignatura_actualizar.modif_usuario = request.session.get("usuario_conectado")
        asignatura_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_asignatura(request):
    if request.method == "POST":
        asignatura_eliminar = Asignatura.objects.get(cod_asignatura=request.POST.get("codigo"))
        asignatura_eliminar.estado = 0
        asignatura_eliminar.modif_usuario = request.session.get("usuario_conectado")
        asignatura_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta



def perfil(request):
    usuario = request.GET.get("codigoPerfil")
    datos_usuario = Usuario.objects.get(cod_usuario=usuario)
    lista_roles = Rol_Usuario.objects.filter(estado=1)
    lista_usuario_rol = Usuario_Rol.objects.filter(estado=1, cod_usuario=usuario)
    lista_carreras = Carrera.objects.all()
    return render(request, "perfil.html", {"datos_usuario": datos_usuario,
                                           "lista_roles": lista_roles,
                                           "lista_usuario_rol": lista_usuario_rol,
                                           "lista_carreras": lista_carreras,
                                           "mensaje_bienvenida": generar_saludo(),
                                           "usuario_conectado": request.session.get("usuario_conectado"),
                                           "nombre_usuario": request.session.get("nombre_del_usuario")})


def asignar_rol(request):
    if request.method == "POST":
        respuesta = ''
        if Usuario_Rol.objects.filter(estado=1, cod_rol_usuario_id=request.POST.get("rol"), cod_carrera_id=request.POST.get("carrera"), cod_usuario_id=request.POST.get("codigo")).exists():
            respuesta = JsonResponse({"bandera": 0,
                                      "mensaje": "El usuario ya cuenta con el rol seleccionado dentro de la carrera"})
            return respuesta
        else:
            nuevo_rol = Usuario_Rol(
                estado=1,
                alta_usuario=request.session.get("usuario_conectado"),
                cod_rol_usuario_id=request.POST.get("rol"),
                cod_usuario_id=request.POST.get("codigo"),
                cod_carrera_id=request.POST.get("carrera")
            )
            nuevo_rol.save()
            lista_roles = Usuario_Rol.objects.filter(
                estado=1, cod_usuario=nuevo_rol.cod_usuario)
            lista_roles = serializers.serialize("json", lista_roles)
            respuesta = JsonResponse({"bandera": 1,
                                      "mensaje": "Rol asignado correctamente.",
                                      "lista_roles": lista_roles})
            return respuesta


@csrf_exempt
def eliminar_rol(request):
    if request.method == 'POST':
        rol = request.POST.get("codigo")
        if Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = rol).exists():
            for asignatura_usuario in Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = rol):
                asignatura_usuario.estado = 0
                asignatura_usuario.save()
        rol_eliminar = Usuario_Rol.objects.get(estado = 1, cod_usuario_rol = rol)
        aux = rol_eliminar.cod_usuario_id
        rol_eliminar.estado = 0
        rol_eliminar.save()
        lista_roles = Usuario_Rol.objects.filter(estado = 1, cod_usuario_id = aux)
        lista_roles = serializers.serialize("json", lista_roles)
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito.",
                                  "lista_roles": lista_roles})
        return respuesta


def detalleAsignaturasCarrera(request):
    cod_carrera = request.GET.get('carrera')
    usuario = request.GET.get('codigo')
    lista_asignaturas = Asignatura.objects.filter(estado = 1, cod_carrera_id = cod_carrera)
    asignaturas_del_usuario = Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = usuario)
    lista_planes = Plan_Estudio.objects.filter(estado = 1)
    lista_asignaturas = serializers.serialize("json", lista_asignaturas)
    asignaturas_del_usuario = serializers.serialize("json", asignaturas_del_usuario)
    lista_planes = serializers.serialize("json", lista_planes)
    return JsonResponse({"lista_asignaturas": lista_asignaturas,
                         "asignaturas_del_usuario": asignaturas_del_usuario,
                         "lista_planes": lista_planes})


@csrf_exempt      
def asignar_asignatura(request):
    if request.method == "POST":
        if Asignatura_Usuario.objects.filter(cod_asignatura_id = request.POST.get("asignatura"), cod_usuario_rol_id = request.POST.get("codigo")).exists():
            reasignar = Asignatura_Usuario.objects.get(cod_asignatura_id = request.POST.get("asignatura"), cod_usuario_rol_id = request.POST.get("codigo"))
            reasignar.estado = 1
            reasignar.modif_usuario = request.session.get("usuario_conectado")
            reasignar.save()
        else:
            nueva_asignatura_usuario = Asignatura_Usuario(
                estado = 1,
                alta_usuario = request.session.get("usuario_conectado"),
                cod_asignatura_id = request.POST.get("asignatura"),
                cod_usuario_rol_id = request.POST.get("codigo")
            )
            nueva_asignatura_usuario.save()        

        lista_asignaturas = Asignatura.objects.filter(estado = 1, cod_carrera_id = request.POST.get("carrera"))
        asignaturas_del_usuario = Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = request.POST.get("codigo"))
        lista_asignaturas = serializers.serialize("json", lista_asignaturas)
        asignaturas_del_usuario = serializers.serialize("json", asignaturas_del_usuario)
        respuesta = JsonResponse({"mensaje": "Asignatura asignada correctamente."})
        return respuesta


@csrf_exempt      
def desvincular_asignatura(request):
    if request.method == "POST":
        desasignar = Asignatura_Usuario.objects.get(estado = 1, cod_asignatura_id = request.POST.get("asignatura"), cod_usuario_rol_id = request.POST.get("codigo"))
        desasignar.estado = 0
        desasignar.modif_usuario = request.session.get("usuario_conectado")
        desasignar.save()
        lista_asignaturas = Asignatura.objects.filter(estado = 1, cod_carrera_id = request.POST.get("carrera"))
        asignaturas_del_usuario = Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = request.POST.get("codigo"))
        lista_asignaturas = serializers.serialize("json", lista_asignaturas)
        asignaturas_del_usuario = serializers.serialize("json", asignaturas_del_usuario)
        respuesta = JsonResponse({"mensaje": "Asignatura desvinculada correctamente."})
        return respuesta

def cabecera(request):
    return render(request, "reporte/cabecera.html")

def metodologia_enseñanza(request):
    return render(request, "metodologia_enseñanza/metodologia_enseñanza.html")

def recurso_auxiliar(request):
    return render(request, "recurso_auxiliar/recurso_auxiliar.html")

def unidad_aprendizaje(request):
    lista_facultades = Facultad.objects.filter(estado=1)
    lista_carreras = Carrera.objects.filter(estado=1)
    lista_asignaturas = Asignatura.objects.filter(estado=1)
    return render(request, "unidad_aprendizaje/unidad_aprendizaje.html", {
                                                     "lista_facultades": lista_facultades,
                                                     "lista_asignaturas": lista_asignaturas,
                                                     "lista_carreras": lista_carreras})

def contenido(request):
    lista_facultades = Facultad.objects.filter(estado=1)
    lista_carreras = Carrera.objects.filter(estado=1)
    lista_asignaturas = Asignatura.objects.filter(estado=1)
    return render(request, "contenido/contenido.html", {
                                                     "lista_facultades": lista_facultades,
                                                     "lista_asignaturas": lista_asignaturas,
                                                     "lista_carreras": lista_carreras})

def tipo_clase(request):
    return render(request, "tipo_clase/tipo_clase.html")

def instrumento_evaluacion(request):
    return render(request, "instrumento_evaluacion/instrumento_evaluacion.html")

def tipo_eva(request):
    return render(request, "tipo_eva/tipo_eva.html")

def trabajo_autonomo(request):
    return render(request, "trabajo_autonomo/trabajo_autonomo.html")

