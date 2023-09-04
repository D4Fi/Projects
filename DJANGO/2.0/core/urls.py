from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('adicionar', views.adicionar),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('produto/<int:pk>/', views.produto, name='produto'),
]
