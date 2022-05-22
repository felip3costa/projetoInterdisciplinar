from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('retorno', views.retorno, name='retorno'),
    path('cadastro_escola', views.cadastro_escola, name='cadastro_escola'),
    path('', views.cadastrar_escola, name='cadastrar_escola'),
    path('cadastro_aluno', views.cadastro_aluno, name='cadastro_aluno'),
    path('login', views.login, name='login'),
    path('', views.cadastrar_aluno, name='cadastrar_aluno')
]