from django.urls import path
from .controllers import (
    crear_historia_clinica,
    listar_historias_clinicas,
    crear_analisis_caso,
    listar_analisis_casos,
    admin_dashboard,
    doctor_dashboard,
    asistente_dashboard
)

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('asistente_dashboard/', asistente_dashboard, name='asistente_dashboard'),
    path('crear_historia/', crear_historia_clinica, name='crear_historia_clinica'),
    path('listar_historias/', listar_historias_clinicas, name='listar_historias_clinicas'),
    path('crear_analisis/', crear_analisis_caso, name='crear_analisis_caso'),
    path('listar_analisis/', listar_analisis_casos, name='listar_analisis_casos'),
    path('administrar_usuarios/', admin_dashboard, name='administrar_usuarios'),
]
