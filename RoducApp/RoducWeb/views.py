from django.shortcuts import render, redirect
from RoducWeb.models import *

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
                    request.session["usuario_conectado"] = datos_usuario.cod_usuario
                    request.session["nombre_del_usuario"] = datos_usuario.nombres_del_usuario 
                    return redirect("inicio")
                else:
                    return render(request, "login.html", {"mensaje_error": "La contraseña ingresada es incorrecta."})
            else:
                return render(request, "login.html", {"mensaje_error": "El usuario no cuenta con los permisos necesarios para acceder."})
        else:
            return render(request, "login.html", {"mensaje_error": "El usuario ingresado no existe."})

def inicio(request):
    return render(request, "inicio.html")
