from django.db.models import Max
from django.apps import apps

class PacienteService:
    @staticmethod
    def generar_hcl():
        Paciente = apps.get_model('pacientes', 'Paciente')  # Obtener modelo sin importar directamente
        max_hcl = Paciente.objects.aggregate(max_hcl=Max('hcl'))['max_hcl']

        # Verifica si hay registros previos y genera el siguiente número
        if max_hcl and max_hcl.isdigit():
            return str(int(max_hcl) + 1)
        return "1"  # Si no hay pacientes, empieza desde "1"