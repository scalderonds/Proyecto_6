from django import forms
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        exclude = ['fecha_creacion']
        # fields = '__all__'
