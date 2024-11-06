from django.contrib import admin
from .models import Usuario, Rol

admin.site.register(Rol)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol', 'telefono', 'direccion', )  # Campos visibles en la lista de usuarios
    search_fields = ('user__username', 'rol__nombre')        # Opciones de búsqueda por nombre de usuario y rol
    list_filter = ('rol',)    
    
