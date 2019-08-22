from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)


def home(request):
    context = {'mensagem': 'Ola munda'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    movRotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'movRotativos': movRotativos})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas})


def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    return render(request, 'core/lista_movmensalistas.html', {'movmensalistas': movmensalistas})
