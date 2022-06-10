from django.urls import path
from restapi import views

urlpatterns = [ 
    path('lista_usuarios', views.UsuarioListAPIView.as_view(), name="usuario_list"),
    path('lista_usuarios/<str:nombre_usuario>', views.UsuarioRetrieveAPIView.as_view(), name="usuario_detail"),
    path('lista_facultades/', views.FacultadListAPIView.as_view(), name="lista_facultades"),
    path('lista_facultades/<int:cod_facultad>', views.FacultadRetrieveAPIView.as_view(), name="facultad_detalle"),
    path('crear_cabecera', views.Cabecera_PlanillaCreateAPIView.as_view(), name="crear_cabecera"),
    path('crear_evaluaciones', views.EvaluacionesCreateAPIView.as_view(), name="crear_evaluaciones"),
    path('cargar_contenidos', views.Contenidos_DadosCreateAPIView.as_view(), name="cargar_contenidos"),
    path('cargar_recursos', views.Recursos_UtilizadosCreateAPIView.as_view(), name="cargar_recursos"),
    path('cargar_trabajos', views.Trabajos_UtilitizadosCreateAPIView.as_view(), name="cargar_trabajos"),
    path('cargar_metodologia', views.Metodologia_UtilizadaCreateAPIView.as_view(), name="cargar_metodologia"),

    #prueba
    path('validarSesion/<int:user>', views.validarSesion, name='validarSesion'),
    #prueba auditoria
    path('auditoriaSesion/<str:user>/<str:info>', views.auditoriaSesion, name='auditoriaSesion'),
    path('listaFacultades_Carreras/<int:user>', views.listaFacultades_Carreras, name='listaFacultades_Carreras'),
    path('historial_reportes/<int:user>', views.historialReportes, name='historial_reportes'),
]