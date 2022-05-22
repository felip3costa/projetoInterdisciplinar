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
    path('', views.cadastrar_aluno, name='cadastrar_aluno')
]

#URLs da área da ESCOLA
urlpatterns += [
    path('escola', views.dash_escola, name='dash_escola'),
    path('e-info', views.e_info, name='e_info'),
    path('e-alunos', views.e_alunos, name='e_alunos'),
    path('e-anoeleitoral', views.e_anoeleitoral, name='e_anoeleitoral'),
    path('e-resultado', views.e_resultado, name='e_resultado'),
    path('e-turmas', views.e_turmas, name='e_turmas')
]