from .models import Paciente
from .services import PacienteService

class PacienteFactory:
    @staticmethod
    def crear_paciente(nombre, apellido, edad, genero, direccion, telefono, email, doctor_actual):
        return Paciente.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            genero=genero,
            direccion=direccion,
            telefono=telefono,
            email=email,
            hcl=PacienteService.generar_hcl(),
            doctor_actual=doctor_actual
        )
