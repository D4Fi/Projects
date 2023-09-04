from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

def index(request):
    if request.method == 'GET':
        return render(request,'core/pages/index.html',
                context={
                    'produto':models.Produto.objects.all(),
                    }
                )

    elif request.method == 'POST':
        pass

def produto(request, pk):
    return render(request,'core/pages/items.html',
            context={
                'item':models.Produto.objects.get(id=pk),
                #'item':get_object_or_404(models.Produto, id=pk),
                }
            )

def delete(request, pk):
    models.Produto.objects.get(id=pk).delete()
    return render(request,'core/pages/delete.html',
            context={
                'produto':models.Produto.objects.all(),
                }
            )

def adicionar(request):
    return render(request,'core/pages/adicionar.html')
