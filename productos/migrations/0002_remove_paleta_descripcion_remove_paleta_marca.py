# Generated by Django 5.0.6 on 2024-07-09 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paleta',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='paleta',
            name='marca',
        ),
    ]