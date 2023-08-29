from django.contrib import admin
from . import models


class Cols(admin.ModelAdmin):
    list_display = ('nome','idade')

admin.site.register(models.Post, Cols)
