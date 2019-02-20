from django.contrib import admin
from .models import TipoServico

class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ['descricao']                                         # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['descricao']                                        # Campos pesquisáveis no admin

admin.site.register(TipoServico, TipoServicoAdmin)
