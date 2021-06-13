# Generated by Django 3.2.4 on 2021-06-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet', models.CharField(max_length=250)),
                ('nombre', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('fechaNacimiento', models.DateTimeField()),
                ('generoPoesia', models.CharField(max_length=250)),
                ('carrera', models.CharField(max_length=250)),
                ('fechaInscripcion', models.DateTimeField()),
                ('fechaExposicion', models.DateTimeField()),
            ],
        ),
    ]
