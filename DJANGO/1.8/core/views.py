from django.shortcuts import render
from .models import Produto

def index(request):
    if request.method == "GET":
        produto = Produto.objects.all()
        context = {'produto': produto}
        return render(request, 'core/pages/index.html', context=context)

def home(request):
    return render(request, 'core/pages/home.html')


def produto(request, pk):
    return render(request, 'core/pages/produto.html')
