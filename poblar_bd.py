#!/usr/bin/env python
"""
Script para poblar la base de datos con datos básicos del sistema DentalSys
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CAO.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import Rol, Usuario
from tratamientos.models import Tratamiento
from pacientes.models import Paciente
from hcl.models import HistoriaClinica
from pacientes.services import PacienteService
from datetime import date, datetime, timedelta
import random

def crear_roles():
    """Crear roles básicos del sistema"""
    roles = ['administrador', 'doctor', 'asistente']
    
    for rol_nombre in roles:
        rol, created = Rol.objects.get_or_create(nombre=rol_nombre)
        if created:
            print(f"✅ Rol '{rol_nombre}' creado")
        else:
            print(f"ℹ️  Rol '{rol_nombre}' ya existe")

def crear_usuarios():
    """Crear usuarios básicos del sistema"""
    # Crear usuario administrador
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@dentalsys.com',
            'first_name': 'Administrador',
            'last_name': 'Sistema',
            'is_staff': True,
            'is_superuser': True
        }
    )
    
    if created:
        admin_user.set_password('dentalsysadmin')
        admin_user.save()
        print("✅ Usuario administrador creado")
    else:
        print("ℹ️  Usuario administrador ya existe")
    
    # Crear perfil de usuario administrador
    try:
        rol_admin = Rol.objects.get(nombre='administrador')
        usuario_admin, created = Usuario.objects.get_or_create(
            user=admin_user,
            defaults={
                'rol': rol_admin,
                'telefono': '+593-99-123-4567',
                'direccion': 'Oficina Principal, Quito'
            }
        )
        if created:
            print("✅ Perfil de administrador creado")
        else:
            print("ℹ️  Perfil de administrador ya existe")
    except Rol.DoesNotExist:
        print("❌ Error: Rol administrador no encontrado")
    
    # Crear usuario doctor
    doctor_user, created = User.objects.get_or_create(
        username='doctor',
        defaults={
            'email': 'doctor@dentalsys.com',
            'first_name': 'Dr. Juan',
            'last_name': 'Pérez',
            'is_staff': True
        }
    )
    
    if created:
        doctor_user.set_password('doctor')
        doctor_user.save()
        print("✅ Usuario doctor creado")
    else:
        print("ℹ️  Usuario doctor ya existe")
    
    # Crear perfil de doctor
    try:
        rol_doctor = Rol.objects.get(nombre='doctor')
        usuario_doctor, created = Usuario.objects.get_or_create(
            user=doctor_user,
            defaults={
                'rol': rol_doctor,
                'telefono': '+593-99-765-4321',
                'direccion': 'Consultorio 1, Clínica DentalSys'
            }
        )
        if created:
            print("✅ Perfil de doctor creado")
        else:
            print("ℹ️  Perfil de doctor ya existe")
    except Rol.DoesNotExist:
        print("❌ Error: Rol doctor no encontrado")

def crear_tratamientos():
    """Crear tratamientos básicos"""
    tratamientos_basicos = [
        {
            'nombre': 'Limpieza Dental',
            'descripcion': 'Limpieza profunda de dientes y encías para eliminar placa y sarro.',
            'costo': 25.00
        },
        {
            'nombre': 'Empaste Dental',
            'descripcion': 'Reparación de caries con material de composite.',
            'costo': 45.00
        },
        {
            'nombre': 'Extracción Dental',
            'descripcion': 'Extracción de diente dañado o problemático.',
            'costo': 35.00
        },
        {
            'nombre': 'Endodoncia',
            'descripcion': 'Tratamiento de conducto radicular para salvar el diente.',
            'costo': 120.00
        },
        {
            'nombre': 'Corona Dental',
            'descripcion': 'Colocación de corona para proteger y restaurar el diente.',
            'costo': 200.00
        },
        {
            'nombre': 'Blanqueamiento Dental',
            'descripcion': 'Procedimiento para blanquear y mejorar la apariencia dental.',
            'costo': 80.00
        }
    ]
    
    for tratamiento_data in tratamientos_basicos:
        tratamiento, created = Tratamiento.objects.get_or_create(
            nombre=tratamiento_data['nombre'],
            defaults={
                'descripcion': tratamiento_data['descripcion'],
                'costo': tratamiento_data['costo']
            }
        )
        if created:
            print(f"✅ Tratamiento '{tratamiento_data['nombre']}' creado")
        else:
            print(f"ℹ️  Tratamiento '{tratamiento_data['nombre']}' ya existe")

def crear_pacientes():
    """Crear pacientes de ejemplo"""
    try:
        # Obtener el doctor para asignar a los pacientes
        doctor_user = User.objects.get(username='doctor')
        
        pacientes_ejemplo = [
            {
                'nombre': 'María',
                'apellido': 'González',
                'edad': 28,
                'genero': 'F',
                'direccion': 'Av. Amazonas 123, Quito',
                'telefono': '+593-99-111-1111',
                'email': 'maria.gonzalez@email.com',
                'doctor_actual': doctor_user
            },
            {
                'nombre': 'Carlos',
                'apellido': 'Ramírez',
                'edad': 35,
                'genero': 'M',
                'direccion': 'Calle 10 de Agosto 456, Quito',
                'telefono': '+593-99-222-2222',
                'email': 'carlos.ramirez@email.com',
                'doctor_actual': doctor_user
            },
            {
                'nombre': 'Ana',
                'apellido': 'López',
                'edad': 42,
                'genero': 'F',
                'direccion': 'Av. 6 de Diciembre 789, Quito',
                'telefono': '+593-99-333-3333',
                'email': 'ana.lopez@email.com',
                'doctor_actual': doctor_user
            },
            {
                'nombre': 'Pedro',
                'apellido': 'Martínez',
                'edad': 55,
                'genero': 'M',
                'direccion': 'Calle García Moreno 321, Quito',
                'telefono': '+593-99-444-4444',
                'email': 'pedro.martinez@email.com',
                'doctor_actual': doctor_user
            },
            {
                'nombre': 'Lucía',
                'apellido': 'Fernández',
                'edad': 31,
                'genero': 'F',
                'direccion': 'Av. República 654, Quito',
                'telefono': '+593-99-555-5555',
                'email': 'lucia.fernandez@email.com',
                'doctor_actual': doctor_user
            }
        ]
        
        pacientes_creados = []
        for paciente_data in pacientes_ejemplo:
            paciente, created = Paciente.objects.get_or_create(
                email=paciente_data['email'],
                defaults=paciente_data
            )
            if created:
                # Generar HCL automáticamente si no se asignó
                if not paciente.hcl:
                    paciente.hcl = PacienteService.generar_hcl()
                    paciente.save()
                print(f"✅ Paciente '{paciente.nombre} {paciente.apellido}' creado (HCL: {paciente.hcl})")
                pacientes_creados.append(paciente)
            else:
                print(f"ℹ️  Paciente '{paciente.nombre} {paciente.apellido}' ya existe")
                pacientes_creados.append(paciente)
        
        return pacientes_creados
        
    except User.DoesNotExist:
        print("❌ Error: Usuario doctor no encontrado. Crea primero los usuarios.")
        return []

def crear_historias_clinicas():
    """Crear historias clínicas de ejemplo"""
    try:
        # Obtener el doctor
        doctor_usuario = Usuario.objects.get(user__username='doctor')
        
        # Obtener todos los pacientes
        pacientes = Paciente.objects.all()
        
        if not pacientes.exists():
            print("❌ No hay pacientes disponibles para crear historias clínicas")
            return
        
        # Obtener algunos tratamientos
        tratamientos = list(Tratamiento.objects.all())
        
        historias_ejemplo = [
            {
                'diagnostico': 'Caries dental en molar superior derecho',
                'sintomas': 'Dolor intenso al masticar, sensibilidad al frío y calor',
                'resultado_exitoso': True
            },
            {
                'diagnostico': 'Gingivitis leve',
                'sintomas': 'Encías inflamadas y sangrado durante el cepillado',
                'resultado_exitoso': True
            },
            {
                'diagnostico': 'Limpieza dental preventiva',
                'sintomas': 'Acumulación de placa y sarro',
                'resultado_exitoso': True
            },
            {
                'diagnostico': 'Extracción de muela del juicio',
                'sintomas': 'Dolor e hinchazón en la zona posterior de la mandíbula',
                'resultado_exitoso': True
            },
            {
                'diagnostico': 'Revisión general',
                'sintomas': 'Control rutinario, sin síntomas específicos',
                'resultado_exitoso': True
            }
        ]
        
        # Crear historias clínicas para cada paciente
        for i, paciente in enumerate(pacientes):
            if i < len(historias_ejemplo):
                historia_data = historias_ejemplo[i]
                
                # Seleccionar un tratamiento aleatorio si hay disponibles
                tratamiento = random.choice(tratamientos) if tratamientos else None
                
                # Fecha de aplicación aleatoria en los últimos 30 días
                fecha_aplicacion = date.today() - timedelta(days=random.randint(1, 30))
                
                historia, created = HistoriaClinica.objects.get_or_create(
                    paciente=paciente,
                    doctor=doctor_usuario,
                    diagnostico=historia_data['diagnostico'],
                    defaults={
                        'sintomas': historia_data['sintomas'],
                        'tratamiento': tratamiento,
                        'fecha_aplicacion_tratamiento': fecha_aplicacion,
                        'resultado_exitoso': historia_data['resultado_exitoso']
                    }
                )
                
                if created:
                    print(f"✅ Historia clínica creada para {paciente.nombre} {paciente.apellido}")
                else:
                    print(f"ℹ️  Historia clínica para {paciente.nombre} {paciente.apellido} ya existe")
    
    except Usuario.DoesNotExist:
        print("❌ Error: Usuario doctor no encontrado en modelo Usuario")
    except Exception as e:
        print(f"❌ Error al crear historias clínicas: {str(e)}")

def main():
    print("🚀 Iniciando poblado de base de datos DentalSys...")
    print("=" * 50)
    
    print("\n📋 Creando roles del sistema...")
    crear_roles()
    
    print("\n👥 Creando usuarios del sistema...")
    crear_usuarios()
    
    print("\n🦷 Creando tratamientos básicos...")
    crear_tratamientos()
    
    print("\n👤 Creando pacientes de ejemplo...")
    pacientes_creados = crear_pacientes()
    
    print("\n📋 Creando historias clínicas de ejemplo...")
    crear_historias_clinicas()
    
    print("\n" + "=" * 50)
    print("✅ ¡Base de datos poblada exitosamente!")
    print("\n📊 Resumen de datos creados:")
    print(f"   👥 Usuarios: {User.objects.count()}")
    print(f"   👤 Pacientes: {Paciente.objects.count()}")
    print(f"   🦷 Tratamientos: {Tratamiento.objects.count()}")
    print(f"   📋 Historias Clínicas: {HistoriaClinica.objects.count()}")
    print("\n📌 Credenciales de acceso:")
    print("   👤 Administrador: admin / dentalsysadmin")
    print("   🩺 Doctor: doctor / doctor")
    print("\n🌐 Ejecuta: python manage.py runserver")
    print("   Y accede a: http://127.0.0.1:8000")

if __name__ == '__main__':
    main()
