from django import forms
from . import models

class B(forms.ModelForm):
    class Meta:
        models = models.A
        fields = ('nome')
