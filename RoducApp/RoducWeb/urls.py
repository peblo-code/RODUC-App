from django.urls import path
from RoducWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name = 'login'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('inicio', views.inicio, name = 'inicio'),

    #USUARIOS
    path('usuario', views.usuario, name='usuario'),
    path('detalle_usuario', views.detalle_usuario, name='detalle_usuario'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),

    #PERFIL
    path('perfil', views.perfil, name='perfil'),
    path('asignar_rol', views.asignar_rol, name='asignar_rol'),
    
    #FACULTAD
    path('facultad', views.facultad, name='facultad'),
    path('agregar_facultad', views.agregar_facultad, name='agregar_facultad'),
    path('detalle_facultad', views.detalle_facultad, name='detalle_facultad'),
    path('actualizar_facultad', views.actualizar_facultad, name='actualizar_facultad'),

    #CARRERA
    path('carrera', views.carrera, name='carrera'),

    #PLAN DE ESTUDIOS
    path('plan_estudio', views.plan_estudio, name='plan_estudio'),

    #SEMESTRES
    path('semestre', views.semestre, name='semestre'),

    #ASIGNATURAS
    path('asignatura', views.asignatura, name='asignatura')
]