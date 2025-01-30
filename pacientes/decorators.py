def formatear_paciente(func):
    def wrapper(*args, **kwargs):
        paciente = func(*args, **kwargs)
        return f"{paciente.nombre} {paciente.apellido} (HCL: {paciente.hcl})"
    return wrapper
