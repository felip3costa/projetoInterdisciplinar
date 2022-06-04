from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retorno', views.retorno, name='retorno'),
    path('cadastro_escola', views.cadastro_escola, name='cadastro_escola'),
    path('', views.cadastrar_escola, name='cadastrar_escola'),
    path('cadastro_aluno', views.cadastro_aluno, name='cadastro_aluno'),
    path('login', views.login, name='login'),
    path('aluno', views.dash_aluno, name='dash_aluno'),
    path('', views.cadastrar_aluno, name='cadastrar_aluno'),
]

#URLs da área da ESCOLA
urlpatterns += [
    path('e_dash', views.e_dash, name='e_dash'),
    path('e_info', views.e_info, name='e_info'),
    path('e_alunos', views.e_alunos, name='e_alunos'),
    path('e_anoeleitoral', views.e_anoeleitoral, name='e_anoeleitoral'),
    path('e_resultado', views.e_resultado, name='e_resultado'),
    path('e_turmas', views.e_turmas, name='e_turmas')
]

#URLs da área do ALUNO
urlpatterns +=[
    path('a_dash', views.a_dash, name='a_dash'),
    path('a_dados', views.a_dados, name='a_dados'),
    path('a_votar', views.a_votar, name='a_votar'),
    path('a_candidatar', views.a_candidatar, name='a_candidatar'),
]