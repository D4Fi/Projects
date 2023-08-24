from django.contrib import admin
from . import models


#admin.site.register(models.Produto, ProdutoAdmin)

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco')



