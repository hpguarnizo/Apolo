from django.db import models
from apps.Usuario.models import Persona

# Create your models here.
class Administrador(models.Model):
    SECTOR_CHOICES = (
        ("1", "Tiene permisos de super administrador"),
        ("0","No tiene permiso"),
    )
    Identificacion = models.CharField(primary_key=True, max_length=25)
    usuario = models.OneToOneField(Persona, null=True, on_delete=models.CASCADE)
    permiso = models.CharField(max_length=85,choices=SECTOR_CHOICES,default="1")

    def __str__(self):
        return self.Identificacion
