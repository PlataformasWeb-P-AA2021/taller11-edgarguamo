from django.forms import ModelForm, models
from django import forms
from django.utils.translation import gettext_lazy as _
from alquiler.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese su nombre completo'),
            'direccion': _('Ingrese su direccion'),
            'cedula': _('Ingresu su cedua'),
            'tipo': _('Ingrese el tipo de edificio'),
        }
    
    def clean_ciudad(self):
        city = self.cleaned_data['ciudad']
        if city[0] == 'L':
            raise forms.ValidationError('Error no existe ciudad con L')
        return city

    def clean_nombre(self):
        propietario = self.cleaned_data['nombre']
        num_palabras = len(propietario.split())
        if num_palabras < 2:
            raise forms.ValidationError('Ingrese al menos un nombre y un apellido')
        return propietario



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'costo_dept', 'num_cuartos', 'edificio']
    
    def clean_costo_dept(self):
        costo = self.cleaned_data['costo_dept']
        if costo > 100000:
            raise forms.ValidationError('Error Cantidad superior a la permitiia')
        return costo
    
    def clean_num_cuartos(self):
        value = self.cleaned_data['num_cuartos']
        if value < 0 or value > 7:
            raise forms.ValidationError('Error Número de cuartos incorrecto')
        return value 
    