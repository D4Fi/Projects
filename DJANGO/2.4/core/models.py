from django.db import models

class ModelsProduto(models.Model):
    logo = models.ImageField()
    produto = models.CharField(max_length=10)
    valor = models.FloatField()
    estoque = models.IntegerField()

