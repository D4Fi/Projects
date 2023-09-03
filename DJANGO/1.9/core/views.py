from django.shortcuts import render
from . import models
from . import forms

def index(request):
    print('==========', request.POST)
    if request.method == 'GET':
        context = {
            'pessoa':models.Pessoa.objects.all(),
            'form':forms.FormPessoa(),
        }
        return render(request, 'core/pages/index.html', context=context)
    
    elif request.method == 'POST':
        models.Pessoa(
                nome=request.POST['nome'],
                idade=request.POST['idade']
                ).save()

        context = {
            'pessoa': models.Pessoa.objects.all(),
            'form':forms.FormPessoa(),
        }
        return render(request, 'core/pages/index.html', context=context)
    
    elif request.method == 'DELETE':
        form = models.Pessoa(
                nome=form['nome'],
                idade=form['idade'],
                )
        form.save()

        pessoa = models.Pessoa.objects.all()
        form = forms.FormPessoa()
        context = {
            'pessoa':pessoa,
            'form':form,
        }
        return render(request, 'core/pages/index.html', context=context)
    
def user(request):
    if request.method == 'GET':
        context = {
            'pessoa':models.Pessoa.objects.all(),
            'form':forms.FormPessoa(),
        }
        return render(request, 'core/pages/user.html', context=context)
 
