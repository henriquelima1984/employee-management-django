from django.db import models


class Funcionario(models.Model):
    # O campo Charfield represneta uma string
    # O campo IntegerField representa um número inteiro positivo
    # O campo DecimalField represneta um número decimal com precisão fixa
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    tempo_de_servico = models.IntegerField(default=0, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    # Será utilizado para fazer operações de busca
    objetos = models.Manager()
