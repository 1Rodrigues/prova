from django.contrib import admin
from .models import Modalidade, Atleta, Tecnico, Equipe

# Register your models here.

class TecnicoInline(admin.TabularInline):
    model = Tecnico

@admin.register(Equipe)
class AdminEquipe(admin.ModelAdmin):
    list_display = ('nome', 'curso')
    inlines = [TecnicoInline,]




@admin.register(Atleta)
class AdminAtleta(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'equipe')
    list_filter = ['nome']
    search_fields = ['nome']

    
admin.site.register(Modalidade)