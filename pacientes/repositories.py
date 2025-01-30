from .models import Paciente

class PacienteRepository:

    @staticmethod
    def obtener_por_id(id):
        return Paciente.objects.get(id=id)

    @staticmethod
    def obtener_todos():
        return Paciente.objects.all() 