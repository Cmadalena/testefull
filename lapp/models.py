from django.db import models


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=100)
    sexo = models.BooleanField()
    tipodoc = models.CharField(max_length=200)
    nrdoc = models.CharField(max_length=200)
    dataadmissao = models.DateField()
    cargo = models.CharField(max_length=200)
    formacaoacademica = models.CharField(max_length=200)
    nivelacademico = models.CharField(max_length=200)
    nuit = models.IntegerField()
    estadocivil = models.CharField(max_length=200)
    localnasc = models.CharField(max_length=200)
    telefone = models.IntegerField()
    telefone1 = models.IntegerField()
    email = models.CharField(max_length=200)
    observacao = models.CharField(max_length=200)



