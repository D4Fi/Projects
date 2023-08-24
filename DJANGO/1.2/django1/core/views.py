from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    context ={'produtos': produtos}
    return render(request,'core/pages/index.html', context=context)

def home(request):
    return render(request,'core/pages/home.html')
