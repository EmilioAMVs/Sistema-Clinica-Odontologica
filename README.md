# DentalSys - Sistema de Gestión para Clínicas Odontológicas

**DentalSys** es un sistema integral diseñado para gestionar pacientes y sus historias clínicas en clínicas odontológicas. El sistema permite optimizar el registro de datos, realizar análisis comparativos de casos históricos, y sugerir tratamientos basados en datos estadísticos.

Accede al proyecto en producción: [DentalSys en Azure](https://dentalsys.azurewebsites.net)

---

## **Características Principales**

### Gestión de Pacientes
- Registro, edición y eliminación de pacientes.
- Organización completa de los datos personales y clínicos.

### Gestión de Tratamientos 
- Registro, edición y eliminacion de tratamientos.
- - Historico de Tratamientos realizadas, con filtros de tipo de tratamiento y fechas.

### Historias Clínicas
- Creación, edición y eliminación de historias clínicas.
- Registro de diagnósticos, síntomas y tratamientos aplicados.
- Indicador de éxito de tratamientos.

### Análisis Comparativo y Sugerencias
- Comparación automática de datos clínicos con casos históricos.
- Generación de sugerencias para tratamientos con base en estadísticas clínicas:
  - Frecuencia de tratamientos similares.
  - Porcentajes de éxito observados.

### Gestión de Usuarios (Solo Administradores)
- Creación y administración de cuentas para usuarios de la clínica:
  - Roles: Administrador, Doctor, Asistente.
- Control total sobre accesos y permisos en el sistema.

### Visualización de Estadísticas
- Datos clave sobre los tratamientos realizados.
- Identificación de tendencias clínicas basadas en casos históricos.

---

## **Credenciales de Prueba**

### **Administrador**
- Usuario: `admin`
- Contraseña: `dentalsysadmin`

### **Doctor**
- Usuario: `doctor`
- Contraseña: `doctor`

---

## **Tecnologías Utilizadas**

### Backend
- **Django 5.1.2**: Framework robusto para la lógica del sistema.
  
### Frontend
- **Bootstrap 5**: Diseño responsivo y limpio.

### Base de Datos
- **PostgreSQL**: Sistema de almacenamiento seguro y escalable.

### Despliegue
- **Azure Web Services**: Plataforma de nube para asegurar alta disponibilidad y escalabilidad.

---

## **Requisitos Previos**

Para configurar el sistema en tu entorno local, asegúrate de contar con:
- **Python** 3.12
- **PostgreSQL** 12 o superior.
- **Git** para clonar el repositorio.
- **Pip** para instalar las dependencias de Python.
- **Virtualenv** (opcional pero recomendado).

---

## **Instalación y Configuración**

### Paso 1: Clonar el Repositorio
Clona el repositorio del proyecto en tu máquina local:

```bash
  git clone https://github.com/usuario/dentalsys.git
  cd dentalsys
```
### Paso 2: Crear un Entorno Virtual
Crea y activa un entorno virtual para aislar las dependencias del proyecto:

```bash
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### Paso 3: Instalar Dependencias
Instala las dependencias necesarias desde el archivo requirements.txt:

```bash
  pip install -r requirements.txt
```

### Paso 4: Configurar la Base de Datos
Configura las credenciales en el archivo settings.py:

```bash
DATABASES = {
  'default': database-connection-string')
}
```

### Paso 5: Aplicar Migraciones
Ejecuta las migraciones para crear las tablas necesarias en la base de datos:

```bash
Paso 5: Aplicar Migraciones
Ejecuta las migraciones para crear las tablas necesarias en la base de datos:
```


### Paso 6: Crear un SuperUsuario
Crea un superusuario para acceder al sistema:

```bash
python manage.py createsuperuser
```

### Paso 7: Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo para probar el sistema localmente:

```bash
  python manage.py runserver
```




