from django.shortcuts import render, redirect
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
    form = TransacaoForm(request.POST or None)                                              # Criando o Form modelado em form.py
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')                                # Redirecionando para listagem.html para não continuar com /nova na URL mesmo após clicar no botão SALVAR 
                                                                            # e duplicidade no cadastro e evitar que salve por cima após retornar e avançar
    data['form'] = form
    return render(request, 'contas/form.html', data)                    # Enviando Form como parâmetro

def update(request, pk):                                                # Parametro recebido pk
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')                                # Redirecionando para listagem.html para não continuar com /nova na URL mesmo após clicar no botão SALVAR 
                                                                            # e duplicidade no cadastro e evitar que salve por cima após retornar e avançar
    data['form'] = form
    return render(request, 'contas/form.html', data)   