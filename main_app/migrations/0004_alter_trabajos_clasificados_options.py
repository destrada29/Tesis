# Generated by Django 4.2.6 on 2023-10-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_trabajos_clasificados'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trabajos_clasificados',
            options={'verbose_name': 'Trabajo', 'verbose_name_plural': 'Trabajos_Clasificados'},
        ),
    ]