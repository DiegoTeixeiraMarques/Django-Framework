from django.contrib import admin
from django.urls import path, include
from .core import urls

urlpatterns = [
    path('', include( urls, namespace='core')),                       # Redireciona para as urls dentro da pasta core do projeto
    path('admin/', admin.site.urls),
]
