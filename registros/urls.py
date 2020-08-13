from django.urls import path
from .views import index, materias


urlpatterns = [
    path('', index, name='index'),
    path('materias/', materias, name='materias')
]
