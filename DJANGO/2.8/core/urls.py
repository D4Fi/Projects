from django.urls import path
from . import views

urlpatterns = [
        path('chart', views.Myviews.as_view(), name='line_chart'),
        path('chartJSON', views.LineChartJSONView.as_view(), name='line_chart_json'),
]
