from django.urls import path
from . import views

urlpatterns = [ 
    path('lista_usuarios', views.UsuarioListAPIView.as_view(), name="usuario_list"),
    path('lista_usuarios/<str:nombre_usuario>', views.UsuarioRetrieveAPIView.as_view(), name="usuario_detail"),
    path('usuario_rol/<int:cod_usuario_id>', views.Usuario_RolRetrieveAPIView.as_view(), name="usuario_rol"),
    path('lista_facultades/', views.FacultadListAPIView.as_view(), name="lista_facultades"),
    path('auditoria_sesion', views.AuditoriaSesionesCreateAPIView.as_view(), name="auditoria_sesion"),    
]