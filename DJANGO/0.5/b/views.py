from django.shortcuts import render


def home(request):
    return render(request, 'b/pages/home.html')


def about(request):
    return render(request, 'b/pages/about.html')


def services(request):
    return render(request, 'b/pages/services.html')


def princing(request):
    return render(request, 'b/pages/princing.html')


def contact(request):
    return render(request, 'b/pages/contact.html')
