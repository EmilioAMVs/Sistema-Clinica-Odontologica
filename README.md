# **Sistema de Gestión Odontológica**

Este sistema es una aplicación web para la gestión de información en una clínica odontológica, diseñado con Django para el backend y Bootstrap para el frontend. El sistema proporciona diferentes vistas según el tipo de usuario (estudiantes, administrativos, docentes y administrador) con funcionalidades específicas para cada uno.

## **Características**

### **1. Gestión de Notas y Tratamientos**
- **Registro de Notas:** Los docentes pueden registrar las notas de los tratamientos realizados por los estudiantes.
- **Registro de Tratamientos:** El personal administrativo puede registrar los tratamientos realizados por los estudiantes, que están vinculados a la historia clínica del paciente.
- **Reportes:** Todos los usuarios con permisos pueden visualizar reportes detallados de las notas y tratamientos, además de visualizar cuantos tratamientos fueron registrados por cada usuario, reporte de notas por niveles de clínica, por estudiante, etc.
- **Historia Clínica:** Cada tratamiento está ligado a la historia clínica del paciente, la cual contiene toda la información relevante, como datos personales y el historial de tratamientos previos.

### **2. Validación de Facturas**
- **Asignación de Tratamientos:** Los tratamientos se asignan a estudiantes mediante un código de factura. Antes de registrar un tratamiento, el sistema valida que el código de factura no haya sido utilizado previamente.

### **3. Vistas por Tipo de Usuario**
- **Estudiantes:** Pueden registrar los tratamientos realizados y ver la información de los pacientes que les han sido asignados.
- **Administrativos:** Pueden gestionar la información de los pacientes y tratamientos, además de generar reportes.
- **Docentes:** Pueden registrar y revisar las notas de los estudiantes, además de supervisar los tratamientos.
- **Administrador:** Tiene acceso a todas las funciones, incluyendo la gestión de usuarios, visualización de reportes generales y administración de las historias clínicas.

## **Tecnologías Utilizadas**

### **Backend:**
- **Django 5.1.1:** Sistema robusto para gestionar la lógica de la aplicación, autenticación de usuarios y gestión de roles.

### **Frontend:**
- **Bootstrap 5:** Para una interfaz visual consistente y responsiva.

### **Base de Datos:**
- **PostgreSQL:** Almacenamiento seguro de datos, incluyendo pacientes, tratamientos, notas y usuarios.

### **Despliegue:**
- **Azure Web Services:** Despliegue en la nube con soporte para escalabilidad y alta disponibilidad.
