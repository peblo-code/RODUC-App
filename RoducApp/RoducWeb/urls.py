from django.urls import path
from RoducWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('inicio', views.inicio, name='inicio'),
    path('asignarFacultad', views.asignarFacultad, name='asignarFacultad'),
    path('error_403', views.error_403, name='error_403'),

    # USUARIOS
    path('usuario', views.usuario, name='usuario'),
    path('detalle_usuario', views.detalle_usuario, name='detalle_usuario'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),
    path('actualizar_usuario', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario', views.eliminar_usuario, name='eliminar_usuario'),

    # PERFIL
    path('perfil', views.perfil, name='perfil'),
    path('asignar_rol', views.asignar_rol, name='asignar_rol'),
    path('eliminar_rol', views.eliminar_rol, name='eliminar_rol'),
    path('detalleAsignaturasCarrera', views.detalleAsignaturasCarrera, name='detalleAsignaturasCarrera'),
    path('asignar_asignatura', views.asignar_asignatura, name='asignar_asignatura'),
    path('desvincular_asignatura', views.desvincular_asignatura, name='desvincular_asignatura'),

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

    # CABECERA
    path('cabecera', views.cabecera, name='cabecera'),

    # METOLODOGIAS DE ENSEÑANZA
    path('metodologia_enseñanza', views.metodologia_enseñanza, name='metodologia_enseñanza'),
    path('agregar_metodologia_enseñanza', views.agregar_metodologia_enseñanza, name='agregar_metodologia_enseñanza'),
    path('detalle_metodologia_enseñanza', views.detalle_metodologia_enseñanza, name='detalle_metodologia_enseñanza'),
    path('actualizar_metodologia_enseñanza', views.actualizar_metodologia_enseñanza, name='actualizar_metodologia_enseñanza'),
    path('eliminar_metodologia_enseñanza', views.eliminar_metodologia_enseñanza, name='eliminar_metodologia_enseñanza'),

    # RECURSOS AUXILIARES
    path('recurso_auxiliar', views.recurso_auxiliar, name='recurso_auxiliar'),
    path('agregar_recurso_auxiliar', views.agregar_recurso_auxiliar, name='agregar_recurso_auxiliar'),
    path('detalle_recurso_auxiliar', views.detalle_recurso_auxiliar, name='detalle_recurso_auxiliar'),
    path('actualizar_recurso_auxiliar', views.actualizar_recurso_auxiliar, name='actualizar_recurso_auxiliar'),
    path('eliminar_recurso_auxiliar', views.eliminar_recurso_auxiliar, name='eliminar_recurso_auxiliar'),

    # UNIDADES DE APRENDIZAJE
    path('unidad_aprendizaje', views.unidad_aprendizaje, name='unidad_aprendizaje'),
    path('agregar_unidad_aprendizaje', views.agregar_unidad_aprendizaje, name='agregar_unidad_aprendizaje'),
    path('detalle_unidad_aprendizaje', views.detalle_unidad_aprendizaje, name='detalle_unidad_aprendizaje'),
    path('actualizar_unidad_aprendizaje', views.actualizar_unidad_aprendizaje, name='actualizar_unidad_aprendizaje'),
    path('eliminar_unidad_aprendizaje', views.eliminar_unidad_aprendizaje, name='eliminar_unidad_aprendizaje'),

    # CONTENIDOS
    path('contenido', views.contenido, name='contenido'),
    path('agregar_contenido', views.agregar_contenido, name='agregar_contenido'),
    path('detalle_contenido', views.detalle_contenido, name='detalle_contenido'),
    path('actualizar_contenido', views.actualizar_contenido, name='actualizar_contenido'),
    path('eliminar_contenido', views.eliminar_contenido, name='eliminar_contenido'),

    # TIPO DE CLASE
    path('tipo_clase', views.tipo_clase, name='tipo_clase'),
    path('agregar_tipo_clase', views.agregar_tipo_clase, name='agregar_tipo_clase'),
    path('detalle_tipo_clase', views.detalle_tipo_clase, name='detalle_tipo_clase'),
    path('actualizar_tipo_clase', views.actualizar_tipo_clase, name='actualizar_tipo_clase'),
    path('eliminar_tipo_clase', views.eliminar_tipo_clase, name='eliminar_tipo_clase'),

    # INSTRUMENTO DE EVALUACION
    path('instrumento_evaluacion', views.instrumento_evaluacion, name='instrumento_evaluacion'),
    path('agregar_instrumento_evaluacion', views.agregar_instrumento_evaluacion, name='agregar_instrumento_evaluacion'),
    path('detalle_instrumento_evaluacion', views.detalle_instrumento_evaluacion, name='detalle_instrumento_evaluacion'),
    path('actualizar_instrumento_evaluacion', views.actualizar_instrumento_evaluacion, name='actualizar_instrumento_evaluacion'),
    path('eliminar_instrumento_evaluacion', views.eliminar_instrumento_evaluacion, name='eliminar_instrumento_evaluacion'),

    # TIPO DE EVALUACION
    path('tipo_eva', views.tipo_eva, name='tipo_eva'),
    path('detalle_tipo_eva', views.detalle_tipo_eva, name='detalle_tipo_eva'),
    path('agregar_tipo_eva', views.agregar_tipo_eva, name='agregar_tipo_eva'),
    path('actualizar_tipo_eva', views.actualizar_tipo_eva, name='actualizar_tipo_eva'),
    path('eliminar_tipo_eva', views.eliminar_tipo_eva, name='eliminar_tipo_eva'),

    # TRABAJO AUTÓNOMO
    path('trabajo_autonomo', views.trabajo_autonomo, name='trabajo_autonomo'),
    path('agregar_trabajo_autonomo', views.agregar_trabajo_autonomo, name='agregar_trabajo_autonomo'),
    path('detalle_trabajo_autonomo', views.detalle_trabajo_autonomo, name='detalle_trabajo_autonomo'),
    path('actualizar_trabajo_autonomo', views.actualizar_trabajo_autonomo, name='actualizar_trabajo_autonomo'),
    path('eliminar_trabajo_autonomo', views.eliminar_trabajo_autonomo, name='eliminar_trabajo_autonomo'),

    # REPORTES
    path('reporte', views.reporte, name='reporte'),
    path('analisisAsignatura', views.analisisAsignatura, name='analisisAsignatura'),
    path('registro_de_operaciones_diarias/<int:cod_cabecera>', views.registro_de_operaciones_diarias, name='registro_de_operaciones_diarias'),
]
