from django.urls import path
from . import views

urlpatterns = [ 
    path('lista_usuarios', views.UsuarioListAPIView.as_view(), name="usuario_list"),
    path('lista_usuarios/<str:nombre_usuario>', views.UsuarioRetrieveAPIView.as_view(), name="usuario_detail"),
    path('auditoria_sesion/', views.AuditoriaSesionesCreateAPIView.as_view(), name="auditoria_sesion"),    
]