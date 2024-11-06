from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.lista_pacientes, name='lista_pacientes'),
    path('<int:paciente_id>/', controllers.detalle_paciente, name='detalle_paciente'),
    path('crear/', controllers.crear_paciente, name='crear_paciente'),
    path('editar/<int:paciente_id>/', controllers.editar_paciente, name='editar_paciente'),
    path('eliminar/<int:paciente_id>/', controllers.eliminar_paciente, name='eliminar_paciente'),
]
