from django.shortcuts import render
from . import forms, models

def index(request):
    return render(request, 'core/pages/index.html')
