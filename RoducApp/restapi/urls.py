from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.UsuarioListAPIView.as_view(), name="usuario_list"), 
]