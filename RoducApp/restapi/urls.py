from django.urls import path
from . import views

urlpatterns = [ 
    path('lista_usuarios', views.UsuarioListAPIView.as_view(), name="usuario_list"),
    path('lista_usuarios/<str:nombre_usuario>', views.PizzeriaRetrieveAPIView.as_view(), name="usuario_detail"),  
]