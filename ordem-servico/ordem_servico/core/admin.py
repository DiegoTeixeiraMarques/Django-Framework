from django.contrib import admin
from .models import TipoServico, Setor, Ugb, Cargo, Funcionario

# ---------------------------------------------------------------- #

class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
admin.site.register(TipoServico, TipoServicoAdmin)

# ---------------------------------------------------------------- #

class SetorAdmin(admin.ModelAdmin):
    list_display = ['centro_custo', 'nome']
    search_fields = ['nome']
admin.site.register(Setor, SetorAdmin)

# ---------------------------------------------------------------- #

class UgbAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome']
    search_fields = ['nome', 'codigo']
admin.site.register(Ugb, UgbAdmin)

# ---------------------------------------------------------------- #

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
admin.site.register(Funcionario, FuncionarioAdmin)

# ---------------------------------------------------------------- #

class CargoAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
admin.site.register(Cargo, CargoAdmin)

# ---------------------------------------------------------------- #

