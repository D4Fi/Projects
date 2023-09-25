from django.contrib import admin
from . import models

i 
 
@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','qt_estoque')
