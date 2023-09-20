from django.db import models

class ModelsProduto(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    img_produto = models.ImageField(upload_to='dados')

    def __str__(self):
        return f'{self.nome}'
