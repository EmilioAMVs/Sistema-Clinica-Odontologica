# Generated by Django 5.1.2 on 2024-10-26 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='AplicacionTratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aplicacion', models.DateTimeField(auto_now_add=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tratamientos.tratamiento')),
            ],
        ),
    ]
