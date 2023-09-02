from django.contrib import admin
from . import models



@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','qt_estoque')
