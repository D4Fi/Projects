from django.shortcuts import render
from . import forms



def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method  == 'GET':
        return render(request, 'contact.html',
                context={
                    'form':forms.ContactForms()
                    }
                )

    elif request.method  == 'POST':
        return render(request, 'contact.html',
                context={
                    'form':forms.ContactForms()
                    }
                )

def product(request):
    return render(request, 'product.html')
