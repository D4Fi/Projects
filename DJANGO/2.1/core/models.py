from django.db import models


class Produto(models.Model):
    name = models.CharField(max_length=100)
    valor = models.FloatField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.name
