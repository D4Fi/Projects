from django.shortcuts import render
from . import models
from . import forms

def index(request):
    dados = models.A.objects.all()
    form = forms.B()
    context ={'dados': dados,'form':form}
    return render(request, 'core/pages/index.html', context=context)
