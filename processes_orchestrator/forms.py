from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'Id',
            'nombre',
            'apellido',
            'ingresos',
            'status',
        ]

        labels = {
            'Id' : 'Id',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'ingresos': 'Ingresos',
            'status': 'Status',
        }

class AprobarSolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['status']  # Solo necesitas el campo 'status' para aprobar la solicitud
        labels = {'status': 'Status'}