from django.db import models

class ModelAnime(models.Model):
    nome = models.CharField(max_length=20)
    img_anime = models.ImageField()
