from django.shortcuts import render
from . import models
from . import forms

















def index(request):
    return render(request, 'core/pages/index.html')

def contact(request):
    form = forms.ContactForms(request.method or None)

    if request.method == 'POST':
        if form.is_valid():
            messages.success(request,'Envioooooooooooooo!!!!!')
            form = forms.ContactForms()
        else:
            messages.error(request,'Errooooorrrrrrrrrrrr!!!!!')

    return render(request, 'core/pages/contact.html',
                  context={
                      'form': forms.ContactForms(),
                      }
                  )

def product(request):
    return render(request, 'core/pages/product.html')
