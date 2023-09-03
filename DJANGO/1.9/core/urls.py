from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('user/', views.user, name='user'),
]
