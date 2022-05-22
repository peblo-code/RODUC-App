from django.urls import path
from RoducWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('inicio', views.inicio, name='inicio'),

    # USUARIOS
    path('usuario', views.usuario, name='usuario'),
    path('detalle_usuario', views.detalle_usuario, name='detalle_usuario'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),
    path('actualizar_usuario', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario', views.eliminar_usuario, name='eliminar_usuario'),

    # PERFIL
    path('perfil', views.perfil, name='perfil'),
    path('asignar_rol', views.asignar_rol, name='asignar_rol'),
    #path('detalleAsignaturasCarrera', views.detalleAsignaturasCarrera, name='detalleAsignaturasCarrera')

    # FACULTAD
    path('facultad', views.facultad, name='facultad'),
    path('agregar_facultad', views.agregar_facultad, name='agregar_facultad'),
    path('detalle_facultad', views.detalle_facultad, name='detalle_facultad'),
    path('actualizar_facultad', views.actualizar_facultad, name='actualizar_facultad'),
    path('eliminar_facultad', views.eliminar_facultad, name='eliminar_facultad'),

    # CARRERA
    path('carrera', views.carrera, name='carrera'),
    path('agregar_carrera', views.agregar_carrera, name='agregar_carrera'),
    path('detalle_carrera', views.detalle_carrera, name='detalle_carrera'),
    path('actualizar_carrera', views.actualizar_carrera, name='actualizar_carrera'),
    path('eliminar_carrera', views.eliminar_carrera, name='eliminar_carrera'),

    # PLAN DE ESTUDIOS
    path('plan_estudio', views.plan_estudio, name='plan_estudio'),
    path('agregar_plan', views.agregar_plan, name='agregar_plan'),
    path('detalle_plan', views.detalle_plan, name='detalle_plan'),
    path('actualizar_plan', views.actualizar_plan, name='actualizar_plan'),
    path('eliminar_plan', views.eliminar_plan, name='eliminar_plan'),

    # SEMESTRES
    path('semestre', views.semestre, name='semestre'),
    path('agregar_semestre', views.agregar_semestre, name='agregar_semestre'),
    path('detalle_semestre', views.detalle_semestre, name='detalle_semestre'),
    path('actualizar_semestre', views.actualizar_semestre, name='actualizar_semestre'),
    path('eliminar_semestre', views.eliminar_semestre, name='eliminar_semestre'),

    # ASIGNATURAS
    path('asignatura', views.asignatura, name='asignatura'),
    path('agregar_asignatura', views.agregar_asignatura, name='agregar_asignatura'),
    path('detalle_asignatura', views.detalle_asignatura, name='detalle_asignatura'),
    path('actualizar_asignatura', views.actualizar_asignatura, name='actualizar_asignatura'),
    path('eliminar_asignatura', views.eliminar_asignatura, name='eliminar_asignatura'),
]
