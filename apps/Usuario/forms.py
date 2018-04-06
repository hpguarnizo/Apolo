from django import forms
import datetime
from apps.Usuario.models import Persona

class Registro_Persona_Form(forms.ModelForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), min_length=4, required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100, required=True)
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
        help_texts = {
            'username': 'Digite su direccion de correo electronico, ejemplo: example@gmail.com.',
            'password': 'Digite su direccion de correo electronico, ejemplo: example@gmail.com.',
        }
        error_messages = {
            'password': {
                'min_length': "La contraseña es muy corta.",
            },
        }
        widgets = {
            'date_joined': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
            'is_active': forms.HiddenInput(attrs={'value':True}),
            'is_staff': forms.HiddenInput(attrs={'value':False}),
            'is_superuser': forms.HiddenInput(attrs={'value':False}),
            'last_login': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
        }
