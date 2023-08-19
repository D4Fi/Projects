from django.shortcuts import render


def home(request):
    return render(request, 'b/pages/home.html')
