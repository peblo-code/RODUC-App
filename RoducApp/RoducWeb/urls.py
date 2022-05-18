from django.urls import path
from RoducWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name = 'login'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('inicio', views.inicio, name = 'inicio'),

    #USUARIOS
    path('usuario/<int:usuario_actual>', views.usuario, name='usuario'),

    #FACULTAD
    path('facultad', views.facultad, name='facultad'),
    path('agregar_facultad', views.agregar_facultad, name='agregar_facultad'),
    path('detalle_facultad', views.detalle_facultad, name='detalle_facultad'),

    #CARRERA
    path('carrera', views.carrera, name='carrera'),

    #PLAN DE ESTUDIOS
    path('plan_estudio', views.plan_estudio, name='plan_estudio'),

    #SEMESTRES
    path('semestre', views.semestre, name='semestre'),

    #ASIGNATURAS
    path('asignatura', views.asignatura, name='asignatura')
]