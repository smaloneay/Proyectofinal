from django import forms
from .models import celular


class celularForm(forms.ModelForm):
    class Meta:
        model = celular
        fields= ["nombre","descripcion","precio","fecha_ingreso","imagen"]
        
        
