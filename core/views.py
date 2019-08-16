from django.shortcuts import render


def home(request):
    context = {'mensagem': 'Ola munda'}
    return render(request, 'core/index.html', context)
