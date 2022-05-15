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
]