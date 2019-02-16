from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']             # Campos que aparecem na listagem dos objetos no admin
    search_fields = ['name', 'slug']                                        # Campos pesquisáveis no admin
    prepopulated_fields = {'slug': ('name',)}                               # Cria string validada para slug em sicronismo com a digitação do usuário

admin.site.register(Course, CourseAdmin)
