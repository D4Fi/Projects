from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.nome} oiiii'
