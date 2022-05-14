from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('retorno', views.retorno, name='retorno'),
    path('cadastro_escola', views.cadastro_escola, name='cadastro_escola'),
    path('', views.cadastrar_escola, name='cadastrar_escola'),
    path('cadastro_aluno', views.cadastro_aluno, name='cadastro_aluno'),
    path('', views.cadastrar_aluno, name='cadastrar_aluno')
]