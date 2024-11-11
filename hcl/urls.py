from django.urls import path
from . import controllers

urlpatterns = [
    path('listar_historias', controllers.listar_historias, name='listar_historias'),
    path('crear_historia/', controllers.crear_historia, name='crear_historia'),
    path('detalle_historia/<int:historia_id>/', controllers.detalle_historia, name='detalle_historia'),
    path('editar_historia/<int:historia_id>/editar/', controllers.editar_historia, name='editar_historia'),
    path('eliminar_historia/<int:historia_id>/eliminar/', controllers.eliminar_historia, name='eliminar_historia'),
]
