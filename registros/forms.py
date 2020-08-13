from django import forms
from .models import MateriaModel, RegistroModel


class MateriaModelForm(forms.ModelForm):
    class Meta:
        model = MateriaModel
        fields  = ['materia']        

class RegistroModelForm(forms.ModelForm):
    class Meta:
        model = RegistroModel
        fields  = ['materia', 'registro']