from django import forms
import datetime
from apps.Usuario.models import Persona
from apps.Administrador.models import Administrador
from django.core import validators

class Registro_Administrador_Form(forms.ModelForm):
    Identificacion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100, required=True)
    
    
    class Meta:
        model = Administrador

        fields = [
            'Identificacion',
            'permiso',
        ]

        labels = {
            'Identificacion':'Identificación del usuario',
            'permiso': 'Permisos del usuario',
        }

        help_texts = {
            'Identificacion': 'Su número de identificación tributaria',
            'permiso': '¿En qué ámbito se genera su actividad económica?.',
            
        }
        widgets = {
            'Identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'permiso': forms.Select(attrs={'class':'form-control'}),
        }

