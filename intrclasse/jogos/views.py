from django.shortcuts import render, get_object_or_404
from .models import Equipe, Modalidade, Atleta, Tecnico

# Create your views here.
def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    context = {
            'equipes': equipes,
            'modalidades':modalidades,
    }
    return render(request, 'index.html', context)

def equipe(request,pk):
    equipe = get_object_or_404(Equipe,pk=pk)
    return render(request, 'equipe.html', {'equipe':equipe})

def modalidade(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)
    return render(request, 'modalidade.html', {'modalidade':modalidade})
    
