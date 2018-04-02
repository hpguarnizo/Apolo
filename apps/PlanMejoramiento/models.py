from django.db import models
from apps.Empresa.models import Empresa

# Create your models here.

class plan(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=25)
    Ruta = models.CharField( max_length=170)
    Empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"plan"
