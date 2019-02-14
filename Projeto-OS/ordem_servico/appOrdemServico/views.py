from django.shortcuts import render, redirect
from .form import TipoServicoForm

def novo_tipo_servico(request):
    dados = {}
    form = TipoServicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_cadastro-tipo-servico')

    dados['form'] = form
    return render(request, 'appOrdemServico/cadastro-tipo-servico.html', dados)
