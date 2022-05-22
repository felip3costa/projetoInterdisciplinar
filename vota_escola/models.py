from django.db import models
from django.contrib.auth.models import User


class Escola(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    nome_escola = models.CharField(max_length=100, null=False)
    rua = models.CharField(max_length=80, null=False)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(max_length=40, null=True, default=None)
    bairro = models.CharField(max_length=40, null=True, default=None)
    cidade = models.CharField(max_length=40, null=True, default=None)
    estado = models.CharField(max_length=40, null=True, default=None)
    cnpj = models.CharField(max_length=18, null=False, unique=True)

    def __str__(self):
        return self.nome_escola

class Turma(models.Model):
    nome_escola = models.ForeignKey(Escola, null=False, on_delete=models.CASCADE)
    turma = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.turma

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(null=True, default=None)
    ra = models.CharField(max_length=20, unique=True, null=False)
    rg = models.CharField(max_length=30, unique=True, null=False)
    status = models.BooleanField(default=False, null=True)
    nome_escola = models.ForeignKey(Escola, null=True, default=None, on_delete=models.CASCADE)
    turma_atual = models.ForeignKey(Turma, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nome_aluno', 'ra', 'rg')

    def __str__(self):
        return str(self.nome_aluno)

class AnoEleicao(models.Model):
    ano = models.IntegerField(null=False)

    def __str__(self):
        return str(self.ano)

class Candidato(models.Model):
    ano = models.ForeignKey(AnoEleicao, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='nome_candidato')
    turma = models.ForeignKey(Turma, null=False, on_delete=models.CASCADE)
    texto_candidatura = models.TextField(null=False)

    class Meta:
        unique_together = ('ano', 'candidato', 'turma')

    def __str__(self):
        return str(self.candidato)

class Votos(models.Model):
    ano = models.ForeignKey(AnoEleicao, null=False, on_delete=models.CASCADE, related_name='ano_eleicao')
    candidato = models.ForeignKey(Candidato, null=False, on_delete=models.CASCADE, related_name='nome')
    eleitor = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='nome_eleitor')

    class Meta:
        unique_together = ('ano', 'candidato', 'eleitor')

