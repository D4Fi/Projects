from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home),
    path('about/',  views.about),
    path('services/',  views.services),
    path('princing/',  views.princing),
    path('contact/',  views.contact),
]
