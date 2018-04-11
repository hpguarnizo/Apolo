from django import forms
import datetime
from apps.Usuario.models import Persona
from apps.Administrador.models import Administrador
from apps.Evaluacion.models import Area
from apps.Evaluacion.models import Indicador
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
            'Nombre': 'Nota: El nombre debe de ser fácilmente identificable, las áreas no pueden tener el mismo nombre.',
            'Descripcion': 'Descripción detallada sobre el área.',
            
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }

class Registro_indicador(forms.ModelForm):
    

    class Meta:
        model = Indicador

        fields = [
            'Nombre',
            'Areas',
        ]

        labels = {
            'Nombre':'Nombre del indicador',
            'Areas': '¿A cuál área pertenece el indicador?',
        }

        help_texts = {
            'Nombre': 'Nota: El nombre debe de ser facilmente identificable, los indicadores no pueden tener el mismo nombre.',
            'Areas': 'Descripción detallada sobre el indicador.',
            
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Areas': forms.Select(attrs={'class':'form-control'}),
        }


