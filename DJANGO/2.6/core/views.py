from django.shortcuts import render
from . import models

def index(request):
    return render(
            request,
            'core/page/index.html',
            context={
                'dados': models.ModelAnime.objects.all(),
                }
            )
