from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaModelForm
from .models import MateriaModel


def index(request):
    """ Renderiza o template da página inicial """
    return render(request, 'index.html')


def materias(request):
    """ Renderiza o template de cadastro de matérias com o
    formulário MaterialModelForm importado de forms.py.
    Verifica se a matéria já há uma matéria com o mesmo nome
    no banco de dados antes de salvar. Exibe uma mensagem de 
    sucesso ou erro ao fim do processo.
     """


    form = MateriaModelForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            mat = form.cleaned_data['materia']
            materia = MateriaModel.objects.filter(materia=mat).first()
            if materia is None:
                form.save()
                messages.success(request, 'Matéria cadastrada com sucesso.')
                form = MateriaModelForm()
            else:
                messages.error(request, 'Esta matéria já foi cadastrada.')

    context = {'form': form}    
    return render(request, 'materias.html', context)