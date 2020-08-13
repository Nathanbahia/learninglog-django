from django.db import models


class MateriaModel(models.Model):
    materia = models.CharField('Matéria', max_length=100)

    class Meta: 
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __str__(self):
        return self.materia
