from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from . import forms

# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dados'] = models.ModelsProduto.objects.all()
        return context
