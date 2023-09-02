from django.urls import path
from . import views 

urlpatterns =[
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('produto/<int:pk>', views.produto, name='baki'),
]
