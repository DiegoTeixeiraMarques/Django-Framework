from django.contrib import admin
from django.urls import path
from appOrdemServico.views import novo_tipo_servico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro-tipo-servico/', novo_tipo_servico, name="url_cadastro-tipo-servico"),
]
