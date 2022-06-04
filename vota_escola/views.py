from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from vota_escola.models import *
from datetime import datetime


# Create your views here.
def home(request):
    dados = {
        'titulo_pagina': 'Página Inicial'
    }
    return render(request, 'home.html', dados)


def retorno(request):
    return render(request, 'retorno.html')


def cadastro_escola(request):

    dados = {
        'nome_formulario': 'Cadastro Escola',
        'titulo_pagina': 'Cadastro Escola'
    }
    return render(request, 'cadastro_escola.html', dados)


def campo_vazio(request, atributo, pagina):
    if not atributo.strip():
        messages.error(request, f'O campo "{atributo}" não pode ficar em branco.')
        return redirect(reverse(pagina))


def password_valido(request, atributo_1, atributo_2, pagina):
    if atributo_1 != atributo_2:
        messages.error(request, 'As senhas devem ser iguais.')
        return redirect(reverse(pagina))


def cnpj_valido(request, cnpj, pagina):
    if Escola.objects.filter(cnpj=cnpj).exists():
        messages.error(request, 'Esse CNPJ já está em uso')
        return redirect(reverse('cadastro_escola'))


def cadastrar_escola(request):
    if request.method == 'POST':
        email = request.POST['email']
        nome_escola = request.POST['nome_escola']
        rua = request.POST['rua']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cnpj = request.POST['cnpj']
        password = request.POST['password']
        repassword = request.POST['repassword']

        campo_vazio(request, 'Nome Escola','cadastro_escola')
        password_valido(request, password, repassword, 'cadastro_escola')
        cnpj_valido(request,cnpj, 'cadastro_escola')

        escola = Escola(
            nome_escola=nome_escola,
            rua=rua,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            cnpj=cnpj,
            password=password
        )
        escola.save()
    return redirect(reverse('cadastro_escola'))


def cadastro_aluno(request):
    dados = {
        'nome_formulario': 'Cadastro Aluno',
        'titulo_pagina': 'Cadastro Aluno'
    }
    return render(request, 'cadastro_escola.html', dados)


def cadastrar_aluno(request):
    messages.success(request, 'Usuário cadastrado com sucesso')
    return redirect(request, 'retorno')


def login(request):
    dados = {
        'nome_formulario': 'login',
        'titulo_pagina': 'Acesso ao ambiente'
    }
    return render(request, 'login.html', dados)


def dash_aluno(request):
    dados = {
        'nome_formulario': 'login',
        'titulo_pagina': 'Acesso ao ambiente'
    }
    return render(request, 'pages/dash_aluno.html', dados)


def e_dash(request):
    dados = {
        'nome_formulario': 'login',
        'titulo_pagina': 'Acesso ao ambiente'
    }
    return render(request, 'pages/escola/inicio.html', dados)


def e_info(request):
    dados = {
        'nome_formulario': 'Dados da Cadastrais',
        'titulo_pagina': 'Dados da Cadastrais'
    }
    return render(request, 'pages/escola/informacoes.html', dados)


def e_turmas(request):
    dados = {
        'nome_formulario': 'Gerenciamento de Turmas',
        'titulo_pagina': 'Gerenciamento de Turmas'
    }
    return render(request, 'pages/escola/turmas.html', dados)


def e_alunos(request):
    dados = {
        'nome_formulario': 'Gerenciamento de Alunos',
        'titulo_pagina': 'Gerenciamento de Alunos'
    }
    return render(request, 'pages/escola/alunos.html', dados)


def e_anoeleitoral(request):
    dados = {
        'nome_formulario': 'Gerenciamento de Eleições',
        'titulo_pagina': 'Gerenciamento de Eleições'
    }
    return render(request, 'pages/escola/anoeleitoral.html', dados)


def e_resultado(request):
    dados = {
        'nome_formulario': 'Resultado das Eleições',
        'titulo_pagina': 'Resultado das Eleições'
    }
    return render(request, 'pages/escola/resultados.html', dados)

def a_dash(request):
    dados = {
        'titulo_pagina': 'Dashboard do Aluno'
    }
    return render(request, 'pages/aluno/inicio.html', dados)

def a_candidatar(request):
    dados = {
        'titulo_pagina': 'Candidate-se'
    }
    return render(request, 'pages/aluno/candidatar.html', dados)

def a_votar(request):
    dados = {
        'titulo_pagina': 'Votar'
    }
    return render(request, 'pages/aluno/votar.html', dados)

def a_dados(request):
    dados = {
        'titulo_pagina': 'Meus Dados'
    }
    return render(request, 'pages/aluno/meusdados.html', dados)
