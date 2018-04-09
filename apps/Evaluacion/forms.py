from django import forms
import datetime
from apps.Usuario.models import Persona
from apps.Administrador.models import Administrador
from apps.Evaluacion.models import Area
from django.core import validators

class Registro_area(forms.ModelForm):


    class Meta:
        model = Area

        fields = [
            'Nombre',
            'Descripcion',
        ]

        labels = {
            'Nombre':'Nombre del área a crear',
            'Descripcion': 'Descripción sobre el área',
        }

        help_texts = {
            'Nombre': 'Nota: El nombre debe de ser facilmente identificable, las áreas no pueden compartir un nombre.',
            'Descripcion': 'Descripción detallada sobre el área',
            
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }


