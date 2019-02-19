from django.shortcuts import render, HttpResponse

def index(request):
    #template_name = 'courses/index.html'
    return HttpResponse('Hello')#render(request, template_name)

