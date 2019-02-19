from django.contrib import admin
from django.urls import path, include
from .core import urls
from .courses import courses_urls

urlpatterns = [
    path('', include( urls, namespace='core')),                       # Redireciona para as urls dentro da pasta core do projeto
    path('cursos/', include(courses_urls, namespace='courses')),
    path('admin/', admin.site.urls),
]
