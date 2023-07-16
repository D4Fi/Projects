from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Meu primeiro progrma com django")
