from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.nome} nome'

class Ficha(models.Model):
    idd = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.idd} i'
