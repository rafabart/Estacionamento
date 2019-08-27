from django.shortcuts import render, redirect
from .forms import PessoaForm
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
    form = PessoaForm()

    data = {'pessoas': pessoas, 'form': form}

    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


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
