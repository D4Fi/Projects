from django.http import HttpResponse
from django.shortcuts import render


nomes = {'x': 'luca', 
         'y': 'vito',
         }


def home(request):
    return render(request, 'b/pages/home.html', context=nomes)


