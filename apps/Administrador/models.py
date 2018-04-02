from django.db import models
from apps.Usuario.models import Persona

# Create your models here.
class Administrador(models.Model):
    Identificacion = models.CharField(primary_key=True, max_length=25)
    usuario = models.OneToOneField(Persona, on_delete=models.CASCADE)
    permiso = models.BooleanField(default=False)

    def __str__(self):
        return self.Identificacion
