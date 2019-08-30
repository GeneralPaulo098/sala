from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    sexo  = models.CharField(max_length=1)
