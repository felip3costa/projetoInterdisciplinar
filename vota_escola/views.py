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
