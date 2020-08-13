from django import forms
from .models import MateriaModel


class MateriaModelForm(forms.ModelForm):
    class Meta:
        model = MateriaModel
        fields  = ['materia']        