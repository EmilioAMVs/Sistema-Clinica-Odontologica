# Generated by Django 5.1.2 on 2024-10-26 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
        ('tratamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasoHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
                ('sintomas', models.TextField()),
                ('frecuencia_prescripcion', models.IntegerField(default=0)),
                ('resultado_exitoso', models.IntegerField(default=0)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tratamientos.tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_exito', models.FloatField()),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('caso_historico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analisis.casohistorico')),
                ('tratamiento_recomendado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tratamientos.tratamiento')),
            ],
        ),
    ]
