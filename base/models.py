from django.db import models

# Create your models here.

# razao_social, atividade_principal, numero_endereco, cep, municipio e estado.

class Empresa(models.Model):
    razao_social = models.CharField(max_length=200)
    atividade_principal = models.CharField(max_length=200)
    numero_endereco = models.IntegerField()
    cep = models.IntegerField()
    municipio = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
