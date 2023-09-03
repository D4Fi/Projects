from django.contrib import admin
from . import models

@admin.register(models.Pessoa)
class AdminPessoa(admin.ModelAdmin):
    list_display = ('nome','idade')

