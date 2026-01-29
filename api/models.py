from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
