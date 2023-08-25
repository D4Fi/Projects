from django.contrib import admin
from . import models

@admin.register(models.Pessoa)
class Test(admin.ModelAdmin):
    date = 'nome'


