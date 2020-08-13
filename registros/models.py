from django.db import models
from datetime import datetime


class MateriaModel(models.Model):
    materia = models.CharField('Matéria', max_length=100)

    class Meta: 
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __str__(self):
        return self.materia

class RegistroModel(models.Model):
    data = models.DateField('Data', default=datetime.now())
    materia = models.ForeignKey('MateriaModel', on_delete=models.CASCADE)
    registro = models.TextField('Registro', max_length=2000)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return '{} - {} - {}'.format(self.data, self.materia, self.registro[:50]+'...')
