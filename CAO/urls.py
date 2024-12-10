"""
URL configuration for CAO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clinica import controllers as clinica_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinica/', include('clinica.urls')),           # Rutas para la app clinica
    path('pacientes/', include('pacientes.urls')),       # Rutas para la app pacientes
    path('tratamientos/', include('tratamientos.urls')), # Rutas para la app tratamientos
    path('usuarios/', include('usuarios.urls')),         # Rutas para la app usuarios
    path('hcl/', include('hcl.urls')),                   # Rutas para la app historias clinicas (hcl)
    path('', clinica_views.home, name='home'),           # Definir home como la vista raíz
]
