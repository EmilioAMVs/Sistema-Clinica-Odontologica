from django.shortcuts import redirect
from functools import wraps     

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_role = getattr(request.user.usuario, 'rol', None)
                if user_role and user_role.nombre in roles:
                    return view_func(request, *args, **kwargs)
            return redirect('/')  # Redirige al inicio si no tiene permisos
        return wrapper
    return decorator

# Decoradores específicos para cada rol
admin_required = role_required(['administrador'])
doctor_required = role_required(['doctor'])
assistant_required = role_required(['ayudante'])
