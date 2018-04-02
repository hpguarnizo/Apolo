from django.db import models
from apps.Usuario.models import Persona

# Create your models here.
class Empresa(models.Model):
    SECTOR_CHOICES = (
        ("Industrial", "Industria"),
        ("Servicios", "Servicio"),
        ("Comercios", "Comercio"),
    )
    NIT = models.CharField(primary_key=True, max_length=60)
    Nombre_empresa = models.CharField(blank=True, max_length=100)
    Sector = models.CharField(max_length=25,choices=SECTOR_CHOICES,default="Comercio")
    Activos = models.CharField(blank=True, max_length=12)
    Numero_empleados = models.CharField(blank=True, max_length=100)
    usuario = models.OneToOneField(Persona,on_delete=models.CASCADE)

    def __str__(self):
        return self.NIT
