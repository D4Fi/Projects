from django.db import models

class ModelsProduto(models.Model):
    nome = models.CharField()
    valor = models.FloatField()


