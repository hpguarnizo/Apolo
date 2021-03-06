# Generated by Django 2.0.3 on 2018-04-02 19:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empresa', '0001_initial'),
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25,  serialize=False)),
                ('Descripcion', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionCompetitividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25, serialize=False)),
                ('Fecha_creacion', models.DateField(default=datetime.datetime.now)),
                ('Descripcion', models.TextField(blank=True, max_length=600)),
                ('Admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.Administrador')),
                ('Areas_Evaluacion', models.ManyToManyField(to='Evaluacion.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35,  serialize=False)),
                ('Areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluacion.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenido', models.TextField(max_length=500,  serialize=False)),
                ('Indicadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluacion.Indicador')),
            ],
        ),
        migrations.CreateModel(
            name='Resultados_Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listado_puntaje', models.CharField(max_length=1000)),
                ('Empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.Empresa')),
                ('evaluaciones', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Evaluacion.EvaluacionCompetitividad')),
            ],
        ),
    ]
