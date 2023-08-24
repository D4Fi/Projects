from django.db import models

class Produto(models.Model):
    nome = models.CharField(
            'Nome',
            max_length=100
            )

    preco = models.DecimalField(
            'Preço',
            max_digits=100,
            decimal_places=3 
            )
    def __str__(self):
        return self.nome
