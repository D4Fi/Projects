from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    qt_estoque = models.IntegerField()

    def __str__(self):
        return self.nome
