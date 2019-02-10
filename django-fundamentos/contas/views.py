from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>Esta é a hora atual %s.</body></html>" %now
    return HttpResponse(html)
