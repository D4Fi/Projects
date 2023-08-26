from django.contrib import admin
from . import models

@admin.register(models.Pessoa)
class Tipo(admin.ModelAdmin):
    nome = 'nome'

@admin.register(models.Ficha)
class Nunber(admin.ModelAdmin):
    idd = 'idd'
    
