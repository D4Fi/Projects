from django.shortcuts import render
from .models import Person


def home(request):
    item = Person.objects.all()
    return render(request, 'b/pages/home.html', context= {'user': item})
