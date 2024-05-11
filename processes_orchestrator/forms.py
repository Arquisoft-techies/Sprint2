from django import forms
from .models import Solicitudes

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'id'
        ]

        labels = {
            'id' : 'Id',
        }