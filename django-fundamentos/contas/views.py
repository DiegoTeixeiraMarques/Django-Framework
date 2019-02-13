from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
import datetime


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>Esta é a hora atual %s.</body></html>" %now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all() 
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm()                                              # Criando o Form modelado em form.py
    data['form'] = form
    return render(request, 'contas/form.html', data)                    # Enviando Form como parâmetro
