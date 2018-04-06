from django import forms
import datetime
from apps.Empresa.models import Empresa

class Registro_empresa_Form(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = [
            'NIT',
            'Nombre_empresa',
            'Sector',
            'Activos',
            'Numero_empleados',
        ]
        labels = {
            'NIT':'NIT',
            'Nombre_empresa':'Nombre de su empresa',
            'Sector':'Sector en el que trabaja su empresa',
            'Activos':'Activos anuales de su empresa',
            'Numero_empleados':'Numero de empleados actuales en su empresa',
        }
        help_texts = {
            'NIT': 'Su Número de Identificación Tributaria',
            'Sector': '¿En qué ambito se genera su actividad economica?.',
            'Activos': 'Activos en millones generados por su empresa en un año, ejemplo: 121.350.255',
        }
        widgets = {
            'NIT': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'Sector': forms.Select(attrs={'class':'form-control'}),
            'Activos': forms.TextInput(attrs={'class':'form-control'}),
            'Numero_empleados': forms.TextInput(attrs={'class':'form-control','value':'1'}),
        }
