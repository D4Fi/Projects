from django.urls import path
from recipes.views import Home


urlpatterns = [
    path('', Home),
]
