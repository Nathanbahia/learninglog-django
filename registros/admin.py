from django.contrib import admin
from .models import MateriaModel, RegistroModel


@admin.register(MateriaModel)
class MateriaModelAdmin(admin.ModelAdmin):
    list_display = ['materia',]

@admin.register(RegistroModel)
class RegistroModelAdmin(admin.ModelAdmin):
    list_display = ['data', 'materia', 'registro']