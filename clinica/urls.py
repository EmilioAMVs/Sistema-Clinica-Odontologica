from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.home, name='home'),
    path('admin_dashboard/', controllers.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', controllers.doctor_dashboard, name='doctor_dashboard'),
    path('ayudante_dashboard/', controllers.ayudante_dashboard, name='ayudante_dashboard'),
    path('administrar_usuarios/', controllers.admin_dashboard, name='administrar_usuarios'),
]
