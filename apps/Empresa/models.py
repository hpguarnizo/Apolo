from django.db import models
from apps.Usuario.models import Persona

# Create your models here.
class Empresa(models.Model):
    SECTOR_CHOICES = (
        ("Industria", "Industria"),
        ("Servicio", "Servicios"),
        ("Comercio", "Comercio"),
    )
    NIT = models.CharField(primary_key=True, max_length=60)
    Nombre_empresa = models.CharField(blank=True, max_length=100)
    Sector = models.CharField(max_length=25,choices=SECTOR_CHOICES,default="Comercio")
    Activos = models.CharField(blank=True, max_length=12)
    Numero_empleados = models.CharField(blank=True, max_length=100)
    usuario = models.OneToOneField(Persona, null=True,on_delete=models.CASCADE)
    Tipo_empresa = models.CharField(null=True, max_length=50)

    def __str__(self):
        return "{} - {}".format(self.NIT, self.Nombre_empresa)
