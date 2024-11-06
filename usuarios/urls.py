from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.home, name='home'),
    path('iniciar_sesion/', controllers.iniciar_sesion, name='iniciar_sesion'),        
    path('cerrar_sesion/', controllers.cerrar_sesion, name='cerrar_sesion'),
    path('listar_usuarios/', controllers.listar_usuarios, name='listar_usuarios'),
    path('detalle_usuario/<int:usuario_id>/', controllers.detalle_usuario, name='detalle_usuario'),
    path('crear_usuario/', controllers.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:usuario_id>/', controllers.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', controllers.eliminar_usuario, name='eliminar_usuario'),  
]
