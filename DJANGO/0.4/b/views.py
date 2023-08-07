from django.shortcuts import render

nomes = {'x': 'luca', 
         'y': 'vito',
         }

def home(request):
    return render(request, 'b/pages/home.html', context=nomes)

def pagina(request,):
    return render(request, 'b/pages/pagina-home.html', context=nomes)
