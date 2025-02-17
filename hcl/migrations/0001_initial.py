# Generated by Django 5.1.2 on 2024-11-11 02:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0002_paciente_doctor_actual_paciente_doctor_derivado_and_more'),
        ('tratamientos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('sintomas', models.TextField()),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('proximo_control', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historias_clinicas', to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias_clinicas', to='pacientes.paciente')),
                ('tratamientos_aplicados', models.ManyToManyField(blank=True, related_name='historias_clinicas', to='tratamientos.aplicaciontratamiento')),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
