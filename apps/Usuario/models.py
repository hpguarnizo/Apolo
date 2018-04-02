from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Persona(AbstractUser):
    campo_vacio = models.CharField(blank=True, max_length=50)