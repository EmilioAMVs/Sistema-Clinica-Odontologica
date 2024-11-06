from django.core.exceptions import PermissionDenied
from .models import Usuario
from django.shortcuts import redirect

def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('signin')
            usuario = Usuario.objects.get(user=request.user)
            if usuario.rol.nombre not in allowed_roles:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
