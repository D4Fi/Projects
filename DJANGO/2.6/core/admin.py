from django.contrib import admin
from . import models

@admin.register(models.ModelAnime)
class AdminAnime(admin.ModelAdmin):
    pass
