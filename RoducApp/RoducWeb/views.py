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
    if (hora_actual >= 6 and hora_actual < 12):
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

#verificador de sesion
def sesion_verificar(request):
    if request.session.get("usuario_conectado"):
        return 1
    else:
        return 0

#convertidor de fecha
def convertirFecha(fecha):
    año = fecha[:(fecha.find('-'))]
    mes = fecha[(fecha.find('-') +1 ): (fecha.find('-') + 3)] 
    dia = fecha[(fecha.find('-') + 4): (fecha.find('-') + 6)] 
    if mes == '01':
        return(dia + ' Enero de ' + año)
    elif mes == '02':
        return(dia + ' Febrero de ' + año)
    elif mes == '03':
        return(dia + ' Marzo de ' + año)
    elif mes == '04':
        return(dia + ' Abril de ' + año)
    elif mes == '05':
        return(dia + ' Mayo de ' + año)
    elif mes == '06':
        return(dia + ' Junio de ' + año)
    elif mes == '07':
        return(dia + ' Julio de ' + año)
    elif mes == '08':
        return(dia + ' Agosto de ' + año)
    elif mes == '09':
        return(dia + ' Septiembre de ' + año)
    elif mes == '10':
        return(dia + ' Octubre de ' + año)
    elif mes == '11':
        return(dia + ' Noviembre de ' + año)
    elif mes == '12':
        return(dia + ' Diciembre de ' + año)
    
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
                    auditar_sesion(request, 'Inicio de sesión en Web')
                    return redirect("inicio")
                else:
                    return render(request, "login.html", {"mensaje_error": "La contraseña ingresada es incorrecta."})
            else:
                return render(request, "login.html", {"mensaje_error": "El usuario no cuenta con los permisos necesarios para acceder."})
        else:
            return render(request, "login.html", {"mensaje_error": "El usuario ingresado no existe."})


def cerrar_sesion(request):
    if request.session.get("usuario_conectado"):
        request.session.flush()
        return redirect("login")
    else:
        return redirect('./')


def inicio(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    mensaje_bienvenida = generar_saludo()
    return render(request, "inicio.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                           "nombre_usuario": request.session.get("nombre_del_usuario"),
                                           "direccion_email": request.session.get("correo_usuario"),
                                           "inicio": 'S',
                                           "mensaje_bienvenida": mensaje_bienvenida})


def usuario(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Usuario.objects.filter(cod_usuario=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_usuario(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        usuario_eliminar = Usuario.objects.get(cod_usuario=request.POST.get("codigo"))
        usuario_eliminar.estado = 0
        usuario_eliminar.modif_usuario = request.session.get("usuario_conectado")
        usuario_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def facultad(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    mensaje_bienvenida = generar_saludo()
    lista_facultad = Facultad.objects.filter(estado=1)
    return render(request, "facultad/facultad.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario"),
                                                      "mensaje_bienvenida": mensaje_bienvenida,
                                                      "lista_facultad": lista_facultad})


def agregar_facultad(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Facultad.objects.filter(cod_facultad=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_facultad(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        print(request.POST.get("codigo"))
        facultad_eliminar = Facultad.objects.get(cod_facultad=request.POST.get("codigo"))
        facultad_eliminar.estado = 0
        facultad_eliminar.modif_usuario = request.session.get("usuario_conectado")
        facultad_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def carrera(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_carreras = Carrera.objects.filter(estado = 1)
    lista_facultades = Facultad.objects.filter(estado = 1)
    return render(request, "carrera/carrera.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario"),
                                                      "mensaje_bienvenida": generar_saludo(),
                                                      "lista_facultades": lista_facultades,
                                                      "lista_carreras": lista_carreras})


def agregar_carrera(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Carrera.objects.filter(cod_carrera=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_carrera(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        carrera_eliminar = Carrera.objects.get(cod_carrera = request.POST.get("codigo"))
        carrera_eliminar.estado = 0
        carrera_eliminar.modif_usuario = request.session.get("usuario_conectado")
        carrera_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def plan_estudio(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Plan_Estudio.objects.filter(cod_plan_estudio=request.GET.get("codigo"))
        carrera = Plan_Estudio.objects.get(cod_plan_estudio=request.GET.get("codigo")).cod_carrera_id
        facultad = Facultad.objects.get(cod_facultad=(Carrera.objects.get(cod_carrera=carrera).cod_facultad_id)).cod_facultad
        detalle = serializers.serialize("json", detalle)

        #facultad = Facultad.objects.get(cod_facultad = (Carrera.objects.get(detalle.cod_facultad).cod_facultad))
        return JsonResponse({"detalle": detalle,
                             "facultad": facultad})


def actualizar_plan(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        plan_eliminar = Plan_Estudio.objects.get(cod_plan_estudio=request.POST.get("codigo"))
        plan_eliminar.estado = 0
        plan_eliminar.modif_usuario = request.session.get("usuario_conectado")
        plan_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def semestre(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_semestre = Semestre.objects.filter(estado=1)
    return render(request, "semestre/semestre.html", {"lista_semestre": lista_semestre,
                                                      "mensaje_bienvenida": generar_saludo(),
                                                      "usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "direccion_email": request.session.get("correo_usuario")})


def agregar_semestre(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Semestre.objects.filter(cod_semestre=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_semestre(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        semestre_eliminar = Semestre.objects.get(cod_semestre=request.POST.get("codigo"))
        semestre_eliminar.estado = 0
        semestre_eliminar.modif_usuario = request.session.get("usuario_conectado")
        semestre_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def asignatura(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Asignatura.objects.filter(cod_asignatura=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def actualizar_asignatura(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        asignatura_eliminar = Asignatura.objects.get(cod_asignatura=request.POST.get("codigo"))
        asignatura_eliminar.estado = 0
        asignatura_eliminar.modif_usuario = request.session.get("usuario_conectado")
        asignatura_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta



def perfil(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        rol = request.POST.get("codigo")
        if Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = rol).exists():
            for asignatura_usuario in Asignatura_Usuario.objects.filter(estado = 1, cod_usuario_rol_id = rol):
                asignatura_usuario.estado = 0
                asignatura_usuario.save()
        rol_eliminar = Usuario_Rol.objects.get(estado = 1, cod_usuario_rol = rol)
        aux = rol_eliminar.cod_usuario_id
        rol_eliminar.modif_usuario = request.session.get("usuario_conectado")
        rol_eliminar.estado = 0
        rol_eliminar.save()
        lista_roles = Usuario_Rol.objects.filter(estado = 1, cod_usuario_id = aux)
        lista_roles = serializers.serialize("json", lista_roles)
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito.",
                                  "lista_roles": lista_roles})
        return respuesta


def detalleAsignaturasCarrera(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
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
    if sesion_verificar(request) == 0:
        return redirect("./")
    return render(request, "reporte/cabecera.html")


def unidad_aprendizaje(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_facultades = Facultad.objects.filter(estado = 1)
    lista_carreras = Carrera.objects.filter(estado = 1)
    lista_asignaturas = Asignatura.objects.filter(estado = 1)
    lista_unidad = Unidad_Aprendizaje.objects.filter(estado = 1)
    lista_planes = Plan_Estudio.objects.filter(estado = 1)
    return render(request, "unidad_aprendizaje/unidad_aprendizaje.html", {"lista_facultades": lista_facultades,
                                                                          "lista_asignaturas": lista_asignaturas,
                                                                          "lista_carreras": lista_carreras,
                                                                          "lista_unidad": lista_unidad,
                                                                          "lista_planes": lista_planes,
                                                                          "mensaje_bienvenida": generar_saludo(),
                                                                          "usuario_conectado": request.session.get("usuario_conectado"),
                                                                          "nombre_usuario": request.session.get("nombre_del_usuario")})


def agregar_unidad_aprendizaje(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        unidad_agregar = Unidad_Aprendizaje(
            numero_unidad = request.POST.get("num_unidad"),
            descripcion = request.POST.get("descripcion"),
            cod_asignatura_id = request.POST.get("asignatura"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado")
        )
        unidad_agregar.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


def detalle_unidad_aprendizaje(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Unidad_Aprendizaje.objects.filter(cod_unidad_aprendizaje=request.GET.get("codigo"))
        carrera = Asignatura.objects.get(cod_asignatura = Unidad_Aprendizaje.objects.get(cod_unidad_aprendizaje = request.GET.get("codigo")).cod_asignatura_id).cod_carrera_id
        facultad = Facultad.objects.get(cod_facultad = Carrera.objects.get(cod_carrera = carrera).cod_facultad_id).cod_facultad
        plan_estudio = Asignatura.objects.get(cod_asignatura = Unidad_Aprendizaje.objects.get(cod_unidad_aprendizaje = request.GET.get("codigo")).cod_asignatura_id).cod_plan_estudio_id
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle,
                             "carrera": carrera,
                             "facultad": facultad,
                             "plan_estudio": plan_estudio})


def actualizar_unidad_aprendizaje(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        unidad_actualizar = Unidad_Aprendizaje.objects.get(estado = 1, cod_unidad_aprendizaje = request.POST.get("codigo"))
        unidad_actualizar.descripcion = request.POST.get("descripcion")
        unidad_actualizar.cod_asignatura_id = request.POST.get("asignatura")
        unidad_actualizar.estado = 1
        unidad_actualizar.modif_usuario = request.session.get("usuario_conectado")
        unidad_actualizar.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta


@csrf_exempt
def eliminar_unidad_aprendizaje(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        unidad_eliminar = Unidad_Aprendizaje.objects.get(cod_unidad_aprendizaje=request.POST.get("codigo"))
        unidad_eliminar.estado = 0
        unidad_eliminar.modif_usuario = request.session.get("usuario_conectado")
        unidad_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def contenido(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_facultades = Facultad.objects.filter(estado=1)
    lista_carreras = Carrera.objects.filter(estado=1)
    lista_asignaturas = Asignatura.objects.filter(estado=1)
    lista_planes = Plan_Estudio.objects.filter(estado=1)
    lista_unidades = Unidad_Aprendizaje.objects.filter(estado=1)
    lista_contenidos = Contenido.objects.filter(estado=1)
    return render(request, "contenido/contenido.html", {"lista_facultades": lista_facultades,
                                                        "lista_asignaturas": lista_asignaturas,
                                                        "lista_carreras": lista_carreras,
                                                        "mensaje_bienvenida": generar_saludo(),
                                                        "usuario_conectado": request.session.get("usuario_conectado"),
                                                        "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                        "lista_planes": lista_planes,
                                                        "lista_unidades": lista_unidades,
                                                        "lista_contenidos": lista_contenidos})

def detalle_contenido(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    detalle = Contenido.objects.filter(estado = 1, cod_contenido = request.GET.get("codigo"))
    unidad = Contenido.objects.get(estado = 1, cod_contenido = request.GET.get("codigo")).cod_unidad_aprendizaje_id
    asignatura = Unidad_Aprendizaje.objects.get(cod_unidad_aprendizaje = unidad, estado = 1).cod_asignatura_id
    carrera = Asignatura.objects.get(cod_asignatura = asignatura, estado = 1).cod_carrera_id
    plan_estudio = Asignatura.objects.get(cod_asignatura = asignatura, estado = 1).cod_plan_estudio_id
    facultad = Carrera.objects.get(cod_carrera = carrera, estado = 1).cod_facultad_id
    detalle = serializers.serialize('json', detalle)
    return JsonResponse({"detalle": detalle,
                         "unidad": unidad,
                         "asignatura": asignatura,
                         "carrera": carrera,
                         "facultad": facultad,
                         "plan_estudio": plan_estudio})


def actualizar_contenido(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    contenido_actualizar = Contenido.objects.get(estado = 1, cod_contenido = request.POST.get("codigo"))
    contenido_actualizar.descripcion = request.POST.get("descripcion")
    contenido_actualizar.cod_unidad_aprendizaje_id = request.POST.get("unidad_aprendizaje")
    contenido_actualizar.estado = 1
    contenido_actualizar.modif_usuario = request.session.get("usuario_conectado")
    contenido_actualizar.save()
    respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
    return respuesta


def agregar_contenido(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    nuevo_contenido = Contenido(
        descripcion = request.POST.get("descripcion"),
        cod_unidad_aprendizaje_id = request.POST.get("unidad_aprendizaje"),
        estado = 1,
        alta_usuario = request.session.get("usuario_conectado")
    )
    nuevo_contenido.save()
    respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
    return respuesta


@csrf_exempt
def eliminar_contenido(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        contenido_eliminar = Contenido.objects.get(cod_contenido=request.POST.get("codigo"))
        contenido_eliminar.estado = 0
        contenido_eliminar.modif_usuario = request.session.get("usuario_conectado")
        contenido_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def tipo_clase(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_tipo = Tipo_Clase.objects.filter(estado = 1)
    return render(request, "tipo_clase/tipo_clase.html", {"mensaje_bienvenida": generar_saludo(),
                                                          "usuario_conectado": request.session.get("usuario_conectado"),
                                                          "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                          "lista_tipo": lista_tipo})


def detalle_tipo_clase(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Tipo_Clase.objects.filter(cod_tipo_clase=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_tipo_clase(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_tipo = Tipo_Clase(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_tipo_clase(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_tipo = Tipo_Clase.objects.get(estado = 1, cod_tipo_clase = request.POST.get("codigo"))
        actualizar_tipo.descripcion = request.POST.get("descripcion")
        actualizar_tipo.estado = 1
        actualizar_tipo.modif_usuario = request.session.get("usuario_conectado")
        actualizar_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_tipo_clase(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        tipo_clase_eliminar = Tipo_Clase.objects.get(cod_tipo_clase=request.POST.get("codigo"))
        tipo_clase_eliminar.estado = 0
        tipo_clase_eliminar.modif_usuario = request.session.get("usuario_conectado")
        tipo_clase_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta
        

def instrumento_evaluacion(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_instrumentos = Instrumento_Evaluacion.objects.filter(estado = 1)
    return render(request, "instrumento_evaluacion/instrumento_evaluacion.html", {"mensaje_bienvenida": generar_saludo(),
                                                                                  "usuario_conectado": request.session.get("usuario_conectado"),
                                                                                  "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                                                  "lista_instrumentos": lista_instrumentos})


def detalle_instrumento_evaluacion(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Instrumento_Evaluacion.objects.filter(cod_instrumento_evaluacion=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_instrumento_evaluacion(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_tipo = Instrumento_Evaluacion(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_instrumento_evaluacion(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_instrumento = Instrumento_Evaluacion.objects.get(estado = 1, cod_instrumento_evaluacion = request.POST.get("codigo"))
        actualizar_instrumento.descripcion = request.POST.get("descripcion")
        actualizar_instrumento.estado = 1
        actualizar_instrumento.modif_usuario = request.session.get("usuario_conectado")
        actualizar_instrumento.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_instrumento_evaluacion(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        instrumento_eliminar = Instrumento_Evaluacion.objects.get(cod_instrumento_evaluacion=request.POST.get("codigo"))
        instrumento_eliminar.estado = 0
        instrumento_eliminar.modif_usuario = request.session.get("usuario_conectado")
        instrumento_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta


def metodologia_enseñanza(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_metodologias = Metodologia_Enseñanza.objects.filter(estado = 1)
    return render(request, "metodologia_enseñanza/metodologia_enseñanza.html", {"mensaje_bienvenida": generar_saludo(),
                                                                                "usuario_conectado": request.session.get("usuario_conectado"),
                                                                                "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                                                "lista_metodologias": lista_metodologias})

def detalle_metodologia_enseñanza(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Metodologia_Enseñanza.objects.filter(cod_metodologia_enseñanza=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_metodologia_enseñanza(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_tipo = Metodologia_Enseñanza(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_metodologia_enseñanza(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_metodologia = Metodologia_Enseñanza.objects.get(estado = 1, cod_metodologia_enseñanza = request.POST.get("codigo"))
        actualizar_metodologia.descripcion = request.POST.get("descripcion")
        actualizar_metodologia.estado = 1
        actualizar_metodologia.modif_usuario = request.session.get("usuario_conectado")
        actualizar_metodologia.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_metodologia_enseñanza(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        instrumento_eliminar = Metodologia_Enseñanza.objects.get(cod_metodologia_enseñanza=request.POST.get("codigo"))
        instrumento_eliminar.estado = 0
        instrumento_eliminar.modif_usuario = request.session.get("usuario_conectado")
        instrumento_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def recurso_auxiliar(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_recursos = Recursos_Auxiliar.objects.filter(estado = 1)
    return render(request, "recurso_auxiliar/recurso_auxiliar.html", {"mensaje_bienvenida": generar_saludo(),
                                                                      "usuario_conectado": request.session.get("usuario_conectado"),
                                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                                      "lista_recursos": lista_recursos})

def detalle_recurso_auxiliar(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Recursos_Auxiliar.objects.filter(cod_recurso_auxiliar=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_recurso_auxiliar(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_tipo = Recursos_Auxiliar(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_recurso_auxiliar(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_metodologia = Recursos_Auxiliar.objects.get(estado = 1, cod_recurso_auxiliar = request.POST.get("codigo"))
        actualizar_metodologia.descripcion = request.POST.get("descripcion")
        actualizar_metodologia.estado = 1
        actualizar_metodologia.modif_usuario = request.session.get("usuario_conectado")
        actualizar_metodologia.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_recurso_auxiliar(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        instrumento_eliminar = Recursos_Auxiliar.objects.get(cod_recurso_auxiliar=request.POST.get("codigo"))
        instrumento_eliminar.estado = 0
        instrumento_eliminar.modif_usuario = request.session.get("usuario_conectado")
        instrumento_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def tipo_eva(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_tipo = Tipo_Eva.objects.filter(estado = 1)
    return render(request, "tipo_eva/tipo_eva.html", {"mensaje_bienvenida": generar_saludo(),
                                                      "usuario_conectado": request.session.get("usuario_conectado"),
                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                      "lista_tipo": lista_tipo})

def detalle_tipo_eva(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Tipo_Eva.objects.filter(cod_tipo_eva=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_tipo_eva(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_tipo = Tipo_Eva(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_tipo_eva(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_tipo = Tipo_Eva.objects.get(estado = 1, cod_tipo_eva = request.POST.get("codigo"))
        actualizar_tipo.descripcion = request.POST.get("descripcion")
        actualizar_tipo.estado = 1
        actualizar_tipo.modif_usuario = request.session.get("usuario_conectado")
        actualizar_tipo.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_tipo_eva(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        tipo_clase_eliminar = Tipo_Eva.objects.get(cod_tipo_eva=request.POST.get("codigo"))
        tipo_clase_eliminar.estado = 0
        tipo_clase_eliminar.modif_usuario = request.session.get("usuario_conectado")
        tipo_clase_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def trabajo_autonomo(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    lista_trabajos = Trabajo_Autonomo.objects.filter(estado = 1)
    return render(request, "trabajo_autonomo/trabajo_autonomo.html", {"mensaje_bienvenida": generar_saludo(),
                                                                      "usuario_conectado": request.session.get("usuario_conectado"),
                                                                      "nombre_usuario": request.session.get("nombre_del_usuario"),
                                                                      "lista_trabajos": lista_trabajos})

def detalle_trabajo_autonomo(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'GET':
        detalle = Trabajo_Autonomo.objects.filter(cod_trabajo_autonomo=request.GET.get("codigo"))
        detalle = serializers.serialize("json", detalle)
        return JsonResponse({"detalle": detalle})


def agregar_trabajo_autonomo(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        nuevo_trabajo = Trabajo_Autonomo(
            descripcion = request.POST.get("descripcion"),
            estado = 1,
            alta_usuario = request.session.get("usuario_conectado"),
        )
        nuevo_trabajo.save()
        respuesta = JsonResponse({"mensaje": "Registro Guardado con Éxito"})
        return respuesta

def actualizar_trabajo_autonomo(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == 'POST':
        actualizar_trabajo = Trabajo_Autonomo.objects.get(estado = 1, cod_trabajo_autonomo = request.POST.get("codigo"))
        actualizar_trabajo.descripcion = request.POST.get("descripcion")
        actualizar_trabajo.estado = 1
        actualizar_trabajo.modif_usuario = request.session.get("usuario_conectado")
        actualizar_trabajo.save()
        respuesta = JsonResponse({"mensaje": "Registro Actualizado con Éxito"})
        return respuesta

@csrf_exempt
def eliminar_trabajo_autonomo(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    if request.method == "POST":
        trabajo_eliminar = Trabajo_Autonomo.objects.get(cod_trabajo_autonomo=request.POST.get("codigo"))
        trabajo_eliminar.estado = 0
        trabajo_eliminar.modif_usuario = request.session.get("usuario_conectado")
        trabajo_eliminar.save()
        respuesta = JsonResponse({"mensaje": "Registro Eliminado con Éxito"})
        return respuesta

def reporte(request):
    if sesion_verificar(request) == 0:
        return redirect("./")
    fecha_actual = str(datetime.today())
    año_actual = fecha_actual[:(fecha_actual.find('-'))]
    print(año_actual + " Año actual")
    mensaje_bienvenida = generar_saludo()
    lista_registros = Cabecera_Planilla.objects.raw('SELECT * FROM "RoducWeb_cabecera_planilla" as c WHERE c.estado = 1 ORDER BY c.fecha_clase desc')
    lista_usuarios = Usuario.objects.filter(estado = 1)
    lista_asignaturas = Asignatura.objects.filter(estado = 1)
    lista_facultades = Facultad.objects.filter(estado = 1)
    lista_carreras = Carrera.objects.filter(estado = 1)
    lista_unidad = Unidad_Aprendizaje.objects.filter(estado = 1)
    lista_planes = Plan_Estudio.objects.filter(estado = 1)
    return render(request, "reporte.html", {"usuario_conectado": request.session.get("usuario_conectado"),
                                           "nombre_usuario": request.session.get("nombre_del_usuario"),
                                           "direccion_email": request.session.get("correo_usuario"),
                                           "mensaje_bienvenida": mensaje_bienvenida,
                                           "lista_registros": lista_registros,
                                           "lista_usuarios": lista_usuarios,
                                           "lista_asignaturas": lista_asignaturas,
                                           "lista_facultades": lista_facultades,
                                           "lista_carreras": lista_carreras,
                                           "lista_unidad": lista_unidad,
                                           "lista_planes": lista_planes})


def registro_de_operaciones_diarias(request, cod_cabecera):
    if sesion_verificar(request) == 0:
        return redirect("./")
    datos_registro = Cabecera_Planilla.objects.get(estado = 1, cod_cabecera_planilla = cod_cabecera)
    datos_asignatura = Asignatura.objects.get(cod_asignatura = datos_registro.cod_asignatura_id)
    datos_carrera = Carrera.objects.get(cod_carrera = datos_asignatura.cod_carrera_id)
    datos_semestre = Semestre.objects.get(cod_semestre = datos_asignatura.cod_semestre_id)
    datos_usuario = Usuario.objects.get(cod_usuario = datos_registro.cod_usuario_id)
    if datos_registro.evaluacion == 0:
        datos_clase = Tipo_Clase.objects.get(cod_tipo_clase = datos_registro.cod_tipo_clase_id)
        lista_unidades = Unidad_Aprendizaje.objects.raw('SELECT DISTINCT u.cod_unidad_aprendizaje, u.descripcion FROM "RoducWeb_contenido" AS c, "RoducWeb_contenidos_dados" AS cd, "RoducWeb_cabecera_planilla" as ca, "RoducWeb_unidad_aprendizaje" AS u WHERE c.cod_contenido = cd.cod_contenido_id AND c.cod_unidad_aprendizaje_id = u.cod_unidad_aprendizaje AND cd.cod_cabecera_planilla_id = ca.cod_cabecera_planilla AND ca.cod_cabecera_planilla = ' + str(cod_cabecera))
        contenidos = Contenido.objects.raw('SELECT c.cod_contenido, c.descripcion, c.cod_unidad_aprendizaje_id FROM "RoducWeb_contenido" AS c, "RoducWeb_contenidos_dados" AS cd WHERE c.cod_contenido = cd.cod_contenido_id AND cd.cod_cabecera_planilla_id = ' + str(cod_cabecera))
        lista_metodologia = Metodologia_Enseñanza.objects.raw('SELECT m.cod_metodologia_enseñanza, m.descripcion FROM "RoducWeb_cabecera_planilla" AS c, "RoducWeb_metodologia_enseñanza" AS m, "RoducWeb_metodologia_utilizada" AS mu WHERE c.cod_cabecera_planilla = mu.cod_cabecera_planilla_id AND mu.cod_metodologia_enseñanza_id = m.cod_metodologia_enseñanza AND c.cod_cabecera_planilla = ' + str(cod_cabecera))
        lista_recurso = Recursos_Auxiliar.objects.raw('SELECT ra.cod_recurso_auxiliar, ra.descripcion FROM "RoducWeb_recursos_auxiliar" AS ra, "RoducWeb_recursos_utilizados" AS ru, "RoducWeb_cabecera_planilla" AS c WHERE c.cod_cabecera_planilla = ru.cod_cabecera_planilla_id and ru.cod_recurso_auxiliar_id = ra.cod_recurso_auxiliar and c.cod_cabecera_planilla = ' + str(cod_cabecera))
        lista_trabajo = Trabajo_Autonomo.objects.raw('SELECT t.cod_trabajo_autonomo, t.descripcion FROM "RoducWeb_trabajo_autonomo" AS t, "RoducWeb_trabajos_utilizados" AS tu, "RoducWeb_cabecera_planilla" AS c where c.cod_cabecera_planilla = tu.cod_cabecera_planilla_id and tu.cod_trabajo_autonomo_id = t.cod_trabajo_autonomo and c.cod_cabecera_planilla = ' + str(cod_cabecera))
        return render(request, "reportes/registro_de_operaciones_diarias.html", {"datos_asignatura": datos_asignatura,
																				"datos_carrera": datos_carrera,
																				"datos_semestre": datos_semestre,
																				"datos_registro": datos_registro,
																				"datos_usuario": datos_usuario,
																				"datos_clase": datos_clase,
																				"lista_unidades": lista_unidades,
																				"contenidos": contenidos,
																				"lista_metodologia": lista_metodologia,
																				"lista_recurso": lista_recurso,
																				"lista_trabajo": lista_trabajo})
    else:
        datos_clase = "Evaluación"
        lista_evaluaciones = Evaluaciones.objects.filter(estado = 1, cod_cabecera_planilla_id = cod_cabecera)
        lista_instrumentos = Instrumento_Evaluacion.objects.all()
        lista_tipo_eva = Tipo_Eva.objects.all()
        return render(request, "reportes/reporte_evaluacion_operacion_diaria.html", {"lista_evaluaciones": lista_evaluaciones,
                                                                                        "lista_instrumentos": lista_instrumentos,
                                                                                        "lista_tipo_eva": lista_tipo_eva,
                                                                                        "datos_asignatura": datos_asignatura,
                                                                                        "datos_carrera": datos_carrera,
                                                                                        "datos_semestre": datos_semestre,
                                                                                        "datos_registro": datos_registro,
                                                                                        "datos_usuario": datos_usuario,
                                                                                        "datos_clase": datos_clase}) 



def analisisAsignatura(request):
    fecha_uno = request.POST.get("fecha_uno")
    fecha_dos = request.POST.get("fecha_dos")
    asignatura = request.POST.get("asignatura")

    datos_asignatura = Asignatura.objects.get(cod_asignatura = asignatura)

    #subcadena para sacar año de fecha uno
    año_uno = fecha_uno[:(fecha_uno.find('-'))]
    #subcadena para sacar año de fecha dos
    año_dos = fecha_dos[:(fecha_dos.find('-'))]

    convertirFecha(fecha_uno)

    #consulta a cabeceras usando los años y fechas como filtro
    cabeceras_fecha_uno = Cabecera_Planilla.objects.raw('SELECT * FROM "RoducWeb_cabecera_planilla" WHERE cod_asignatura_id = ' + str(asignatura) + " and fecha_clase BETWEEN '" + str(año_uno) + '-01-01\' AND \'' + str(fecha_uno) + '\' and estado = 1 and evaluacion = 0 ORDER BY fecha_clase')
    cabeceras_fecha_dos = Cabecera_Planilla.objects.raw('SELECT * FROM "RoducWeb_cabecera_planilla" WHERE cod_asignatura_id = ' + str(asignatura) + " and fecha_clase BETWEEN '" + str(año_dos) + '-01-01\' AND \'' + str(fecha_dos) + '\' and estado = 1 and evaluacion = 0 ORDER BY fecha_clase')
    
    #consulta para traer las unidades que se dieron en las fechas
    unidades_fecha_uno = Unidad_Aprendizaje.objects.raw('SELECT DISTINCT u.cod_unidad_aprendizaje, u.descripcion, cont.fecha FROM "RoducWeb_unidad_aprendizaje" AS u, (SELECT c.cod_contenido, c.descripcion, c.cod_unidad_aprendizaje_id, cau.fecha_clase AS fecha FROM "RoducWeb_contenidos_dados" AS cd, "RoducWeb_contenido" AS c, (SELECT * FROM "RoducWeb_cabecera_planilla" AS cp WHERE cp.cod_asignatura_id = ' + str(asignatura) + ' AND cp.fecha_clase BETWEEN \'' + str(año_uno) + '-01-01\' AND \'' + str(fecha_uno) + '\' AND cp.estado = 1) AS cau WHERE cau.cod_cabecera_planilla = cd.cod_cabecera_planilla_id AND cd.estado = 1 AND cd.cod_contenido_id = c.cod_contenido) AS cont WHERE u.cod_unidad_aprendizaje = cont.cod_unidad_aprendizaje_id ORDER BY cont.fecha')
    unidades_fecha_dos = Unidad_Aprendizaje.objects.raw('SELECT DISTINCT u.cod_unidad_aprendizaje, u.descripcion, cont.fecha FROM "RoducWeb_unidad_aprendizaje" AS u, (SELECT c.cod_contenido, c.descripcion, c.cod_unidad_aprendizaje_id, cau.fecha_clase AS fecha FROM "RoducWeb_contenidos_dados" AS cd, "RoducWeb_contenido" AS c, (SELECT * FROM "RoducWeb_cabecera_planilla" AS cp WHERE cp.cod_asignatura_id = ' + str(asignatura) + ' AND cp.fecha_clase BETWEEN \'' + str(año_dos) + '-01-01\' AND \'' + str(fecha_dos) + '\' AND cp.estado = 1) AS cau WHERE cau.cod_cabecera_planilla = cd.cod_cabecera_planilla_id AND cd.estado = 1 AND cd.cod_contenido_id = c.cod_contenido) AS cont WHERE u.cod_unidad_aprendizaje = cont.cod_unidad_aprendizaje_id ORDER BY cont.fecha')
    
    #consulta para traer los contenidos que se dieron en las fechas 
    contenidos_fecha_uno = Contenido.objects.raw('SELECT DISTINCT c.cod_contenido, c.descripcion, c.cod_unidad_aprendizaje_id, cau.fecha_clase AS fecha FROM "RoducWeb_contenidos_dados" AS cd, "RoducWeb_contenido" AS c, (SELECT * FROM "RoducWeb_cabecera_planilla" AS cp WHERE cp.cod_asignatura_id = ' + str(asignatura) + ' AND cp.fecha_clase BETWEEN \'' + str(año_uno) + '-01-01\' AND \'' + str(fecha_uno) + '\' AND cp.estado = 1) AS cau WHERE cau.cod_cabecera_planilla = cd.cod_cabecera_planilla_id AND cd.estado = 1 AND cd.cod_contenido_id = c.cod_contenido')
    contenidos_fecha_dos = Contenido.objects.raw('SELECT DISTINCT c.cod_contenido, c.descripcion, c.cod_unidad_aprendizaje_id, cau.fecha_clase AS fecha FROM "RoducWeb_contenidos_dados" AS cd, "RoducWeb_contenido" AS c, (SELECT * FROM "RoducWeb_cabecera_planilla" AS cp WHERE cp.cod_asignatura_id = ' + str(asignatura) + ' AND cp.fecha_clase BETWEEN \'' + str(año_dos) + '-01-01\' AND \'' + str(fecha_dos) + '\' AND cp.estado = 1) AS cau WHERE cau.cod_cabecera_planilla = cd.cod_cabecera_planilla_id AND cd.estado = 1 AND cd.cod_contenido_id = c.cod_contenido')

    #todos los contenidos de la materia
    todos_contenidos = Contenido.objects.raw('SELECT c.cod_contenido FROM "RoducWeb_unidad_aprendizaje" as u, "RoducWeb_contenido" as c WHERE c.cod_unidad_aprendizaje_id = u.cod_unidad_aprendizaje AND u.cod_asignatura_id = ' + str(asignatura))
    todos_contenidos = len(list(todos_contenidos))

    #total de contenidos dados
    total_dado_uno = len(list(contenidos_fecha_uno))
    total_dado_dos = len(list(contenidos_fecha_dos))

    #promedios
    promedio_uno = round((total_dado_uno * 100) / todos_contenidos)
    promedio_dos = round((total_dado_dos * 100) / todos_contenidos)

    return render(request, "reportes/analisis_asignatura.html", {"cabeceras_fecha_uno": cabeceras_fecha_uno,
                                                                 "cabeceras_fecha_dos": cabeceras_fecha_dos,
                                                                 "unidades_fecha_uno": unidades_fecha_uno,
                                                                 "unidades_fecha_dos": unidades_fecha_dos,
                                                                 "contenidos_fecha_uno": contenidos_fecha_uno,
                                                                 "contenidos_fecha_dos": contenidos_fecha_dos,
                                                                 "fecha_uno": convertirFecha(fecha_uno),
                                                                 "fecha_dos": convertirFecha(fecha_dos),
                                                                 "año_uno": año_uno,
                                                                 "año_dos": año_dos,
                                                                 "datos_asignatura": datos_asignatura,
                                                                 "promedio_uno": promedio_uno,
                                                                 "promedio_dos": promedio_dos,
                                                                 "total_dado_uno": total_dado_uno,
                                                                 "total_dado_dos": total_dado_dos,
                                                                 "todos_contenidos": todos_contenidos})