from django.db import models
import datetime
from apps.Administrador.models import Administrador
from apps.Empresa.models import Empresa

# Create your models here.

class Area(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=25)
    Descripcion = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.Nombre

class Indicador(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=35)
    Areas = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Pregunta(models.Model):
    Contenido = models.TextField(primary_key=True, max_length=500)
    Indicadores = models.ForeignKey(Indicador, on_delete=models.CASCADE)

    def __str__(self):
        return self.Contenido

class EvaluacionCompetitividad(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=25)
    Fecha_creacion = models.DateField(default=datetime.datetime.now)
    Descripcion = models.TextField(blank=True, max_length=600)
    Areas_Evaluacion = models.ManyToManyField(Area)
    Admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre



class Resultados_Evaluacion(models.Model):
    Listado_puntaje = models.CharField(max_length=1000)
    evaluaciones = models.OneToOneField(EvaluacionCompetitividad, on_delete=models.CASCADE)
    Empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.evaluaciones.Nombre