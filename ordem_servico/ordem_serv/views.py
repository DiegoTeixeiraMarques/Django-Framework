from django.shortcuts import render
from .models import TipoServico

def home(request):
    lista = {}
    lista['tipos'] = TipoServico.objects.all()
    return render(request, 'ordem_serv/home', lista)
