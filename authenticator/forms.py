from django import forms
from .models import Login
from .models import Signup

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'nombres',
            'apellidos',
            'pais',
            'ciudad',
            'correo',
            'numero',
        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'pais': 'País',
            'ciudad': 'Ciudad',
            'correo': 'Correo',
            'numero': 'Número',
        }
            

class SingupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = [
            'profesion',
            'activiad',
            'empresa',
            'ingresos',
            'deudas',
        ]
        labels = {
            'profesion': 'Profesión',
            'activiad': 'Actividad Económica',
            'empresa': 'Empresa',
            'ingresos': 'Ingresos',
            'deudas': 'Deudas',
            }
            
        