from django.shortcuts import render, get_object_or_404
from .models import CasoHistorico, Recomendacion

# Listado de casos históricos
def lista_casos_historicos(request):
    casos_historicos = CasoHistorico.objects.all()
    return render(request, 'analisis/lista_casos_historicos.html', {'casos_historicos': casos_historicos})

# Detalle y generación de recomendaciones para un caso histórico
def detalle_caso_historico(request, caso_id):
    caso = get_object_or_404(CasoHistorico, id=caso_id)
    recomendaciones = Recomendacion.objects.filter(caso_historico=caso)
    return render(request, 'analisis/detalle_caso_historico.html', {'caso': caso, 'recomendaciones': recomendaciones})
