from django import forms
import datetime
from apps.Usuario.models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'date_joined',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
        ]
        labels = {
            'username':'Correo Electronico',
            'password': 'Contraseña',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }
        widgets = {
            'username': forms.TextInput(attrs={'name':'user','class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'date_joined': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
            'is_active': forms.HiddenInput(attrs={'value':True}),
            'is_staff': forms.HiddenInput(attrs={'value':False}),
            'is_superuser': forms.HiddenInput(attrs={'value':False}),
            'last_login': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
        }
