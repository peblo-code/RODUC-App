from django.urls import path
from restapi import views

urlpatterns = [ 
    path('lista_usuarios', views.UsuarioListAPIView.as_view(), name="usuario_list"),
    path('lista_usuarios/<str:nombre_usuario>', views.UsuarioRetrieveAPIView.as_view(), name="usuario_detail"),
    path('usuario_rol/<int:cod_usuario_id>', views.Usuario_RolRetrieveAPIView.as_view(), name="usuario_rol"),
    path('lista_facultades/', views.FacultadListAPIView.as_view(), name="lista_facultades"),
    path('lista_facultades/<int:cod_facultad>', views.FacultadRetrieveAPIView.as_view(), name="facultad_detalle"),
    path('auditoria_sesion', views.AuditoriaSesionesCreateAPIView.as_view(), name="auditoria_sesion"),    


    #prueba
    path('validarSesion/<int:user>', views.validarSesion, name='validarSesion'),
    #prueba auditoria
    path('auditoriaSesion/<str:user>/<str:info>', views.auditoriaSesion, name='auditoriaSesion')
]