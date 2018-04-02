from django.contrib import admin
from apps.Evaluacion import models

# Register your models here.
admin.site.register(models.EvaluacionCompetitividad)
admin.site.register(models.Area)
admin.site.register(models.Indicador)
admin.site.register(models.Pregunta)
admin.site.register(models.Resultados_Evaluacion)