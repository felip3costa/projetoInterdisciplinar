from django.contrib import admin

from vota_escola.models import *


# Register your models here.
admin.site.register(Escola)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Candidato)
admin.site.register(AnoEleicao)

@admin.register(Votos)
class Eleicao(admin.ModelAdmin):
    list_display = ('ano', 'candidato', 'eleitor')
