from django.contrib import admin
from . import models

@admin.register(models.ModelsProduto)
class AdminProduto(admin.ModelAdmin):
    pass

