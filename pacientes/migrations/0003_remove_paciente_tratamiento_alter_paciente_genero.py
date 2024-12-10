# Generated by Django 5.1.2 on 2024-12-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_doctor_actual_paciente_doctor_derivado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='tratamiento',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
