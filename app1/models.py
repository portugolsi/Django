from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preco", decimal_places=2, max_digits=8)
    qtdEstoque = models.IntegerField("Quantidade em Estoque")

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("email", max_length=254)
