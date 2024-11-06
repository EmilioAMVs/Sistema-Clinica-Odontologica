from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from .models import Usuario
from .forms import UsuarioForm
from clinica.decorators import admin_required, doctor_required, assistant_required

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {
            'form': AuthenticationForm()
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if usuario is None:
            return render(request, 'iniciar_sesion.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, usuario)
            
            # Verificar el rol del usuario y redirigir al dashboard correspondiente
            usuario_detalle = Usuario.objects.get(user=usuario)
            if usuario_detalle.rol.nombre == 'admin':
                return redirect('admin_dashboard')  # Ruta para el dashboard del administrador
            elif usuario_detalle.rol.nombre == 'doctor':
                return redirect('doctor_dashboard')  # Ruta para el dashboard del estudiante
            elif usuario_detalle.rol.nombre == 'ayudante':
                return redirect('ayudante_dashboard')  # Ruta para el dashboard del profesor
            else:
                return redirect('base')  # Ruta de inicio para otros casos


def cerrar_sesion(request):
    logout(request)
    return redirect('base')

@admin_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

@admin_required
@admin_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'El usuario ha sido creado exitosamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Error al crear el usuario. Intenta nuevamente.'})
    
    # En el caso de una solicitud GET, renderizamos el formulario vacío
    form = UsuarioForm()
    
    # Obtener el token CSRF
    csrf_token = get_token(request)
    
    # Renderizar el formulario y pasar el token CSRF
    form_html = render_to_string('crear_usuario_form.html', {'form': form, 'csrf_token': csrf_token})
    
    return JsonResponse({'form_html': form_html})


@admin_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Usuario actualizado correctamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Error al actualizar el usuario.'})
    
    else:
        form = UsuarioForm(instance=usuario)
    
    # Enviar el formulario con los valores actuales para mostrarlo en el modal de SweetAlert
    form_html = render_to_string('editar_usuario_form.html', {'form': form})
    return JsonResponse({'form_html': form_html})


@admin_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})