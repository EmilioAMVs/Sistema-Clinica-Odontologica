# Generated by Django 5.1.2 on 2024-12-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamientos', '0002_remove_tratamiento_costo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='fecha_aplicacion',
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]