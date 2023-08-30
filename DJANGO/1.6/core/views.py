from django.shortcuts import render
from . import models
from . import forms


def index(request):

    if request.method == 'GET':
        pessoa = models.Pessoa.objects.all()
        form = forms.UserPost()
        context = {'pessoa': pessoa, 'forms': form}
        return render(request, 'core/pages/index.html', context=context)

    elif request.method == 'POST':
        form = forms.UserPost(request.POST)
        if form.is_valid:
            form.save()
            pessoa = models.Pessoa.objects.all()
            form = forms.UserPost()
            context = {'pessoa': pessoa, 'forms': form}
            return render(request, 'core/pages/index.html', context=context)
