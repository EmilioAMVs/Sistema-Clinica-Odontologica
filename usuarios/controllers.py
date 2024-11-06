from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Usuario
from .forms import CustomUserCreationForm, CustomUserEditForm
from clinica.decorators import admin_required, doctor_required, assistant_required

def home(request):
    return render(request, 'home.html')

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
            usuario_detalle = Usuario.objects.get(user=usuario)
            if usuario_detalle.rol.nombre == 'admin':
                return redirect('admin_dashboard')
            elif usuario_detalle.rol.nombre == 'doctor':
                return redirect('doctor_dashboard')
            elif usuario_detalle.rol.nombre == 'ayudante':
                return redirect('ayudante_dashboard')
            else:
                return redirect('home')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@admin_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

@admin_required
def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'crear_usuario.html', {'form': CustomUserCreationForm()})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('listar_usuarios')
        else:
            return render(request, 'crear_usuario.html', {
                'form': form,
                'error': 'Error en los datos. Intenta nuevamente.'
            })

@admin_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'GET':
        form = CustomUserEditForm(instance=usuario)
        return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})
    else:
        form = CustomUserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('listar_usuarios')
        else:
            return render(request, 'editar_usuario.html', {
                'form': form,
                'usuario': usuario,
                'error': 'Error al actualizar el usuario. Intenta nuevamente.'
            })

@admin_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

@admin_required
def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    user = usuario.user 

    context = {
        'usuario': usuario,
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
        'rol': usuario.rol,
        'telefono': usuario.telefono,
        'direccion': usuario.direccion,
    }
    return render(request, 'detalle_usuario.html', context)