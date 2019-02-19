from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .core import urls
from .courses import courses_urls
from django.conf.urls.static import static

urlpatterns = [
    path('', include( urls, namespace='core')),                       # Redireciona para as urls dentro da pasta core do projeto
    path('cursos/', include(courses_urls, namespace='courses')),
    path('admin/', admin.site.urls),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)