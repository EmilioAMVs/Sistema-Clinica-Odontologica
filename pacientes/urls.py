from django.urls import path
from . import controllers

urlpatterns = [
    path('listar_pacientes/', controllers.listar_pacientes, name='listar_pacientes'),
    path('detalle_paciente/<int:paciente_id>/', controllers.detalle_paciente, name='detalle_paciente'),
    path('crear_paciente/', controllers.crear_paciente, name='crear_paciente'),
    path('editar_paciente/<int:paciente_id>/', controllers.editar_paciente, name='editar_paciente'),
    path('eliminar_pacientes/<int:paciente_id>/', controllers.eliminar_paciente, name='eliminar_paciente'),
]
