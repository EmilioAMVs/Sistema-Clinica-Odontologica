import pandas as pd
from .models import CasoHistorico

def comparar_paciente(nueva_historia):
    """
    Compara los datos de una nueva historia clínica con casos históricos
    y genera recomendaciones de tratamiento basadas en coincidencias.
    
    Args:
        nueva_historia (dict): Diccionario con los datos del nuevo paciente.
            Debe contener claves como 'edad', 'genero' y 'sintomas' (lista de síntomas).

    Returns:
        recomendaciones (list): Lista de recomendaciones ordenadas por relevancia.
        Ejemplo de retorno:
        [
            {
                'tratamiento': 'Tratamiento X',
                'frecuencia_prescripcion': 20,
                'porcentaje_exito': 85.0
            },
            ...
        ]
    """
    # Variables de configuración
    margen_edad = 5  # Rango de tolerancia de edad
    peso_edad = 1.0  # Peso para la variable edad
    peso_genero = 1.0  # Peso para la coincidencia de género
    peso_sintomas = 2.0  # Peso para cada síntoma coincidente

    # Obtener todos los casos históricos
    casos = CasoHistorico.objects.all()
    
    # Crear lista de recomendaciones con puntaje
    recomendaciones = []

    for caso in casos:
        # Calcular coincidencias
        score = 0
        
        # 1. Coincidencia de edad
        if abs(caso.edad - nueva_historia['edad']) <= margen_edad:
            score += peso_edad
        
        # 2. Coincidencia de género
        if caso.genero == nueva_historia['genero']:
            score += peso_genero
        
        # 3. Coincidencia de síntomas
        sintomas_coincidentes = set(caso.sintomas.split(',')) & set(nueva_historia['sintomas'])
        score += len(sintomas_coincidentes) * peso_sintomas
        
        # Si el puntaje es suficientemente alto, se considera relevante
        if score > 0:
            recomendaciones.append({
                'tratamiento': caso.tratamiento,
                'frecuencia_prescripcion': caso.frecuencia_prescripcion,
                'porcentaje_exito': calcular_porcentaje_exito(caso),
                'score': score
            })

    # Ordenar las recomendaciones por el puntaje (de mayor a menor relevancia)
    recomendaciones.sort(key=lambda x: x['score'], reverse=True)
    
    # Retornar la lista de recomendaciones
    return recomendaciones

def calcular_porcentaje_exito(caso):
    """
    Calcula el porcentaje de éxito de un caso histórico basado en datos almacenados.

    Args:
        caso (CasoHistorico): Instancia del caso histórico.

    Returns:
        float: Porcentaje de éxito del tratamiento.
    """
    # Puedes personalizar este cálculo según los datos disponibles en tu modelo
    if caso.frecuencia_prescripcion > 0:
        return (caso.resultado_exitoso / caso.frecuencia_prescripcion) * 100
    else:
        return 0.0
