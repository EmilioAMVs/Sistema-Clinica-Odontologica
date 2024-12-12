from django.urls import path
from . import controllers

urlpatterns = [
    path('listar_tratamientos', controllers.lista_tratamientos, name='listar_tratamientos'),
    path('crear_tratamiento/', controllers.crear_tratamiento, name='crear_tratamiento'),
    path('editar_tratamiento/<int:tratamiento_id>/', controllers.editar_tratamiento, name='editar_tratamiento'),
    path('eliminar_tratamiento/<int:tratamiento_id>/', controllers.eliminar_tratamiento, name='eliminar_tratamiento'),
    path('historial_tratamientos/', controllers.historial_tratamientos, name='historial_tratamientos'),
]
