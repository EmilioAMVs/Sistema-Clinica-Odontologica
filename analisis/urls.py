from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.lista_casos_historicos, name='lista_casos_historicos'),
    path('<int:caso_id>/', controllers.detalle_caso_historico, name='detalle_caso_historico'),
]
