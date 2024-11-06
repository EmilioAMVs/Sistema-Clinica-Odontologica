from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.lista_tratamientos, name='lista_tratamientos'),
    path('crear/', controllers.crear_tratamiento, name='crear_tratamiento'),
    path('editar/<int:tratamiento_id>/', controllers.editar_tratamiento, name='editar_tratamiento'),
    path('eliminar/<int:tratamiento_id>/', controllers.eliminar_tratamiento, name='eliminar_tratamiento'),
]
