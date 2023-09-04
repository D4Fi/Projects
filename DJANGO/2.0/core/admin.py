from django.contrib import admin
from . import models


@admin.register(models.Produto)
class AdminProduto(admin.ModelAdmin):
    model = models.Produto
    list_display = ('name', 'valor','estoque')
