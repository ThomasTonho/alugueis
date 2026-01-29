from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)


class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    locador = models.ForeignKey(Usuario, related_name='imoveis', on_delete=models.CASCADE)

class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    locador = models.ForeignKey(Usuario, related_name='contratos_locador', on_delete=models.CASCADE)
    locatario = models.ForeignKey(Usuario, related_name='contratos_locatario', on_delete=models.CASCADE)