from django.contrib import admin
from curriculo.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display('nome','sigla', 'tipo')

admin.site.register (Curso,CursoAdmin)

