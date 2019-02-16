from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {}
    data['usuario'] = 'Diego'
    return render(request, 'home.html', data)
