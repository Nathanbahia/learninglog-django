from django.contrib import admin
from .models import MateriaModel


@admin.register(MateriaModel)
class MateriaModelAdmin(admin.ModelAdmin):
    list_display = ['materia',]