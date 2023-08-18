from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.nome}'
